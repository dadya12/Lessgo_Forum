from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView
from webapp.models import Answers, Topics
from webapp.forms import AnswerForm


class AnswerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'Answers/answer_create.html'
    model = Answers
    form_class = AnswerForm

    def form_valid(self, form):
        topic = get_object_or_404(Topics, pk=self.kwargs.get('pk'))
        answer = form.save(commit=False)
        answer.topic = topic
        answer.author = self.request.user
        answer.save()
        topic.answers_count += 1
        topic.save()
        return redirect('webapp:topic_detail', pk=topic.pk)
