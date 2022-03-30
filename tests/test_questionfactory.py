from qcm.qcmmodel.models import Animals, animals_dict
from qcm.qcmmodel.question_creator import QuestionFactory, QCMQuestion


class TestQuestionFactory:

    def test_question_factory(self):
        animals = Animals(**animals_dict)
        factory = QuestionFactory(animals)
        question = factory.get_random_question()
        print(question.json())
