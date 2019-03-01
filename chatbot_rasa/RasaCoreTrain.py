from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy
from rasa_core.agent import Agent

# this will catch predictions the model isn't very certain about
# there is a threshold for the NLU predictions as well as the action predictions
fallback = FallbackPolicy(fallback_action_name="action_default_fallback",core_threshold=0.2,nlu_threshold=0.2)
agent = Agent('domain.yml', policies=[MemoizationPolicy(), KerasPolicy(), fallback])
training_data = agent.load_data('stories.md')
agent.train(
    training_data,
    validation_split=0.0
)
agent.persist('models/dialogue')

    