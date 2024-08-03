from django.urls import path
from webapp.views.topics import HomePageView, CreateTopicView, TopicDetailView
from webapp.views.answers import AnswerCreateView

app_name = 'webapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreateTopicView.as_view(), name='topic_create'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topics/<int:pk>/ansewr/', AnswerCreateView.as_view(), name='answer_create'),
]
