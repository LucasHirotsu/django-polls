from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy

@login_required # controle de acesso usando o decorador de função
def sobre(request):
    return HttpResponse('Este é um app de enquete!')

# controle de acesso usando o mecanismo de herança que torna o login obrigatório
class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
        }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse(f"Resultados da pergunta de número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Você vai votar na pergunta de número {question_id}")

class QuestionCreateView(CreateView):
    model = Question
    fields = ('question_text',)
    success_url = reverse_lazy('question-list')
    template_name = 'polls/question_form.html'

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy("question_list")