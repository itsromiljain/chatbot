import logging
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.evaluate import run_evaluation


def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename='rasa_nlu.log', level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, project_name='current', fixed_model_name='nlu')
    run_evaluation('./data/nlu.md', model_directory)


def run_nlu():
    logging.basicConfig(filename='rasa_nlu.log', level=logging.DEBUG)
    interpreter = Interpreter.load('./models/current/nlu')
    print(interpreter.parse("Hello"))


if __name__ == '__main__':
    train_nlu('./data/nlu.md', 'nlu_config.yml', './models')
    run_nlu()
