from pydantic import BaseModel
import random
from qcm.models import Animal, RegimeAlimentaire

class QCMQuestion(BaseModel):
    question: str
    answers: list[str]
    correct_answer: str


class QuestionFactory:

    def __init__(self):
        self.animals = Animal.objects.all()
        self.regimes = RegimeAlimentaire.objects.all()

    def _get_random_regime_names(self) -> list[str]:
        random_regime = random.sample(list(self.regimes), 4)
        random_regime_names = [regime.name for regime in random_regime]
        return random_regime_names

    def get_random_question(self) -> QCMQuestion:
        animal = random.choice(self.animals)
        while animal.regime_alimentaire.name not in (random_regime_names := self._get_random_regime_names()):
            continue

        return QCMQuestion(
            question=f"Quel régime alimentaire a cet animal : {animal.name} ?",
            answers=random_regime_names,
            correct_answer=animal.regime_alimentaire.name
        )

