from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass

    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config)
        model_trainer.train()