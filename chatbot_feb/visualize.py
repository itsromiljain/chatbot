from rasa_core.agent import Agent
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy


fallback = FallbackPolicy(core_threshold=0.2, nlu_threshold=0.1, fallback_action_name='utter_default')


def visualize(domain_file, training_data_file):
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(), fallback])
    agent.visualize(training_data_file, output_file='graphs/graph.html', max_history=2)


if __name__ == '__main__':
    visualize('domain.yml', 'data/stories.md')
