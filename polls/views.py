from django.shortcuts import get_object_or_404, HttpResponse, render
from django.template import loader
from django.views import generic

from .models import Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "most_recent_questions"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def ResultsView(generic.DetailView):
#     model = Question
#     template = "polls/detail.html"
def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
