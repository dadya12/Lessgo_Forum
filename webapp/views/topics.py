from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView, DetailView
from webapp.models import Topics
from webapp.forms import TopicForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = Topics
    template_name = 'home.html'
    context_object_name = 'topics'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created')


class CreateTopicView(LoginRequiredMixin, CreateView):
    model = Topics
    template_name = 'Topics/topic_create.html'
    form_class = TopicForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:home')


class TopicDetailView(DetailView):
    model = Topics
    template_name = 'Topics/topic_detail.html'






