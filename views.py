from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.utils import timezone



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    a=5
    if request.method=='POST':
      y=request.POST['see']
      if y=='sagar':
        a=2
     
    return render(request, 'polls/detail.html', {'question': question, 'a':a})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    q = Question(question_text="Where", pub_date=timezone.now())  
    q.save()
    
    return HttpResponse("You're voting on question %s." % question_id)
