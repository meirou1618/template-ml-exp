from domain.data import TemplateData
from domain.experiment import Experiment


class ModelTrainer:
    @staticmethod
    def train(experiment: Experiment, train_data: TemplateData):
        model = experiment.model
        trained_model = model.ml_model.fit(train_data)
        experiment.model.update_model(trained_model)
        experiment.mark_trained()


class ModelPredictor:
    def predict(self, experiment: Experiment, input_data):
        return experiment.model.ml_model.predict(input_data)
