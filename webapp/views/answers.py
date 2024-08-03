from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
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


class AnswerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Answers
    form_class = AnswerForm
    permission_required = 'webapp.change_answer'
    template_name = 'Answers/answer_update.html'

    def has_permission(self):
        answer = self.get_object()
        return super().has_permission() and self.request.user == answer.author

    def get_success_url(self):
        return reverse('webapp:topic_detail', kwargs={'pk': self.object.topic.pk})


class AnswerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Answers
    permission_required = 'webapp.delete_answer'
    template_name = 'Answers/answer_delete.html'

    def has_permission(self):
        answer = self.get_object()
        return super().has_permission() and self.request.user == answer.author

    def post(self, request, *args, **kwargs):
        answer = self.get_object()
        topic = answer.topic
        response = super().post(request, *args, **kwargs)
        topic.answers_count -= 1
        topic.save()

        return response

    def get_success_url(self):
        return reverse('webapp:topic_detail', kwargs={'pk': self.object.topic.pk})
