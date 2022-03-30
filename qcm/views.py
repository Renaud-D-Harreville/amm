from django.shortcuts import render
from django.views import View
from qcm.qcmmodel.question_creator import QuestionFactory, QCMQuestion
from .forms import QCMForm
import json


class IndexView(View):
    form_class = QCMForm
    template_name = 'qcm/index.html'

    def _get_new_question(self) -> QCMQuestion:
        factory = QuestionFactory()
        question = factory.get_random_question()
        return question

    def _get_form_from_question(self, question: QCMQuestion):
        form = self.form_class()
        form.fields['answers'].choices = [(index, answer) for index, answer in enumerate(question.answers)]
        form.fields['question'].initial = question.dict()
        return form

    def get(self, request):
        question = self._get_new_question()
        form = self._get_form_from_question(question)
        return render(request, self.template_name, {"question": question, "form": form})

    def post(self, request):

        question_dict = json.loads(request.POST["question"])
        question = QCMQuestion(**question_dict)
        answer_indexes = [int(index) for index in request.POST.getlist('answers')]
        form = self._get_form_from_question(question)
        if question.is_correct_answer(answer_indexes):
            to_print = "Bonne réponse !"
        else:
            to_print = f"Mauvaise réponse ! Les bonnes réponses étaient : " \
                       f"{list(index + 1 for index in question.correct_answer_indexes)}"
        return render(request, self.template_name,
                      {"question": question,
                          'form': form,
                       'response': to_print
                       }
                      )
