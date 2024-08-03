from django.urls import path
from webapp.views.topics import HomePageView, CreateTopicView, TopicDetailView, TopicUpdateView, TopicDeleteView
from webapp.views.answers import AnswerCreateView, AnswerUpdateView, AnswerDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreateTopicView.as_view(), name='topic_create'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topics/<int:pk>/ansewr/', AnswerCreateView.as_view(), name='answer_create'),
    path('topics/<int:pk>/update/', TopicUpdateView.as_view(), name='topic_update'),
    path('topics/<int:pk>/delete/', TopicDeleteView.as_view(), name='topic_delete'),
    path('answers/<int:pk>/', AnswerUpdateView.as_view(), name='answer_update'),
    path('answers/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer_delete'),
]
