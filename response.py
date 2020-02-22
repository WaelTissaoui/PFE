import pymongo
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu.components import ComponentBuilder
import random

class response(object):
    INTENT_Salutation = "salutation"
    salutation_msg = ['ahla','salut','ahla cv ?']
    
    def __init__(self,config_file,data_file,model_dir):
        self.config_file=config_file
        self.data_file=data_file
        self.rasa_config=config.load(config_file)
        self.model_dir=model_dir

    def train(self):
        train_data=load_data(self.data_file)
        trainer=Trainer(self.rasa_config)
        trainer.train(train_data)
        self.interpreter=Interpreter.load(trainer.persist(self.model_dir))
        print('trained successfully')

    def parse(self,msg):
        return self.interpreter.parse(msg)

    def reply (self,msg):
        res=self.parse(msg)
        if res["intent"]["name"] == self.INTENT_Salutation:
            return random.choice(self.salutation_msg)














