from django.shortcuts import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from webapp.models import Topics
from webapp.forms import TopicForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


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


class TopicUpdateView(PermissionRequiredMixin, UpdateView):
    model = Topics
    form_class = TopicForm
    template_name = 'Topics/topic_update.html'
    permission_required = 'webapp.change_topic'

    def has_permission(self):
        topic = self.get_object()
        return super().has_permission() and self.request.user == topic.author

    def get_success_url(self):
        return reverse('webapp:topic_detail', kwargs={'pk': self.object.pk})


class TopicDeleteView(PermissionRequiredMixin, DeleteView):
    model = Topics
    template_name = 'Topics/topic_delete.html'
    permission_required = 'webapp.delete_topic'
    success_url = reverse_lazy('webapp:home')

    def has_permission(self):
        topic = self.get_object()
        return super().has_permission() and self.request.user == topic.author




