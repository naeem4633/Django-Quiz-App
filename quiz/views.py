from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render 
from .models import Question


class IndexView(TemplateView):
    template_name = 'quiz/index.html'

def take_quiz(request):
    questions_list = Question.objects.all()
    context = {'questions_list' : questions_list}
    return render(request, 'quiz/takequiz.html', context)   

# def result(request):
#     questions = Question.objects.all()
#     answers = {}

#     for question in questions:
#         answer_key = 'answer_{}'.format(question.id)
#         answers[question.id] = request.POST.get(answer_key, None) 

#     correct_answers = {1: "Yes", 2: "No", 3: "Yes"}

#     if answers == correct_answers:
#         context = {'result': 'pass'}
#     else:
#         context = {'result': 'fail'}

#     return render(request, 'quiz/result.html', context)

def result(request):
    questions = Question.objects.all()
    answers = {}

    for question in questions:
        answer_key = 'answer_{}'.format(question.id)
        answers[question.id] = request.POST.get(answer_key, None)

    correct_answers = {1: "Yes", 2: "No", 3: "Yes"}

    is_passed = True
    for question_id, answer in answers.items():
        if correct_answers.get(question_id) != answer:
            is_passed = False
            break

    if is_passed:
        context = {'result': 'pass'}
    else:
        context = {'result': 'fail'}

    return render(request, 'quiz/result.html', context)


# class QuizUpdateView(UpdateView):
#     # question = Question.objects.all()
#     # fields = [question.question_choice]