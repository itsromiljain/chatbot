import logging
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.evaluate import run_evaluation


logfile = 'nlu_model.log'


def train_nlu(data_path, configs, model_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    training_data = load_data(data_path)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_path, project_name='current', fixed_model_name='nlu')
    run_evaluation(data_path, model_directory)


def run_nlu(nlu_path):
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    interpreter = Interpreter.load(nlu_path)
    pprint.pprint(interpreter.parse("Can you please tell me some news around the world?"))
    pprint.pprint(interpreter.parse("What is going on around the glob?"))
    pprint.pprint(interpreter.parse("Tell me some news in tech?"))
    pprint.pprint(interpreter.parse("Tell me some news in tech space?"))
    pprint.pprint(interpreter.parse("Tell me some news in Tech Space?"))
    pprint.pprint(interpreter.parse("Please tell me What is going on around the Glob?"))
    pprint.pprint(interpreter.parse("What is cooking in technology?"))


if __name__ == '__main__':
    # train_nlu('./data/nlu.md', 'nlu_config.yml', './models')
    run_nlu('./models/current/nlu')
