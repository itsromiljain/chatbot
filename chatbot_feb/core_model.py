import logging
import yaml
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig


fallback = FallbackPolicy(core_threshold=0.2, nlu_threshold=0.1,fallback_action_name='utter_default')


def train_core(domain_file, model_path, training_data_file):
    logging.basicConfig(filename='rasa_core.log', level=logging.DEBUG)
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(), fallback])
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return agent


def run_core(core_model_path, nlu_model_path):
    logging.basicConfig(filename='rasa_core.log', level=logging.DEBUG)
    nlu_interpreter = RasaNLUInterpreter(nlu_model_path)
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load(core_model_path, interpreter=nlu_interpreter, action_endpoint=action_endpoint)
    input_channel = SlackInput('')
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
    print(yaml.safe_load('endpoints.yml'))
    train_core('domain.yml', './models/dialogue', './data/stories.md')
    run_core('./models/dialogue', './models/current/nlu')
