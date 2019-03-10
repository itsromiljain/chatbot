import logging
from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter


fallback = FallbackPolicy(core_threshold=0.2, nlu_threshold=0.1,fallback_action_name='utter_default')


def train_core(domain_file, model_path, training_data_file):
    logging.basicConfig(level='INFO')
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(), fallback])
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return agent


def run_core(core_model_path, nlu_model_path):
    logging.basicConfig(level='INFO')
    nlu_interpreter = RasaNLUInterpreter(nlu_model_path)
    agent = Agent.load(core_model_path, interpreter=nlu_interpreter)
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
    train_core('domain.yml', './models/dialogue', './data/stories.md')
    run_core('./models/dialogue', './models/current/nlu')
