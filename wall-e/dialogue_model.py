import logging
from rasa_core import config
from rasa_core import utils
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


logfile = 'dialogue_model.log'


def train_core(domain_file, model_path, training_data_file, policy_config):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    agent = Agent(domain_file, policies=config.load(policy_config))
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return agent


def run_core(core_model_path, nlu_model_path, action_endpoint_url, slack_token):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    nlu_interpreter = RasaNLUInterpreter(nlu_model_path)
    action_endpoint = EndpointConfig(url=action_endpoint_url)
    agent = Agent.load(core_model_path, interpreter=nlu_interpreter, action_endpoint=action_endpoint)
    input_channel = SlackInput(slack_token)
    agent.handle_channels([input_channel], 5004, serve_forever=True)

    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_text(a)
        for response in responses:
            print(response["text"])
    return agent


if __name__ == '__main__':
    actionConfig = utils.read_yaml_file('endpoints.yml')
    slackConfig = utils.read_yaml_file('credentials.yml')
    train_core('domain.yml', './models/dialogue', './data/stories.md', 'policy.yml')
    run_core('./models/dialogue', './models/current/nlu',
             actionConfig["action_endpoint"]["url"], slackConfig["slack"]["slack_token"])
