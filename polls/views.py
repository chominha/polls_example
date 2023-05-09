from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    print(latest_question_list)
    return render(request, 'polls/index.html', context)

#큐형식으로 저장된 데이터를 선입선출을 위해서 -(역순)pub_data으로 끌고 들어옴.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: #예외 처리하는 것.
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #set.all 전부 set.get 선택해서 가져옴
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_massage':"you didn't select a choice."})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):  #polls/result?q.id=5
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question' : question}) #최종결과물을 보여줌
