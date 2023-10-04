from django.urls import path
from . import views
urlpatterns = [
    # # ex: 127.0.0.1:8000/polls/
    # path("", views.index, name="index"),

    # # ex: 127.0.0.1:8000/polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),

    # # ex: 127.0.0.1:8000/polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),

    # # ex: 27.0.0.1:8000/polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # página de cadastro de nova enquete
    path('cadastrar', views.QuestionCreateView.as_view(), name="question-create"),   
    path('listar', views.QuestionListView.as_view(), name="question-list"),
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail"),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name="question-delete"),
    path('<int:pk>/atualizar', views.QuestionUpdateView.as_view(), name='question-update')
    
]

