from django.urls import path
from webapp.views import HomePageView, CreateTopicView

app_name = 'webapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create/', CreateTopicView.as_view(), name='topic_create'),
]
