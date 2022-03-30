from pydantic import BaseModel
import random
from qcm.models import Animal, RegimeAlimentaire


class QCMQuestion(BaseModel):
    question: str
    answers: list[str]
    correct_answer_indexes: list[int]

    def add_answer_number_prefix(self):
        for i in range(len(self.answers)):
            suffix = f"{i + 1}: "
            if self.answers[i][:3] == suffix:  # if already done.
                continue
            self.answers[i] = f"{suffix}{self.answers[i]}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_answer_number_prefix()

    def is_correct_answer(self, answer_indexes: list[int]):
        if len(answer_indexes) != len(self.correct_answer_indexes):
            return False
        for answer in answer_indexes:
            if answer not in self.correct_answer_indexes:
                return False
        return True


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
            question=f"Quel est le régime alimentaire de cet animal : {animal.name} ?",
            answers=random_regime_names,
            correct_answer_indexes=[random_regime_names.index(animal.regime_alimentaire.name)]
        )

