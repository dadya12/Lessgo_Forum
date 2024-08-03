from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView
from webapp.models import Topics
from webapp.forms import TopicForm, SearchForm
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = Topics
    template_name = 'home.html'
    context_object_name = 'topics'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        self.search_value = None
        if self.search_form.is_valid():
            self.search_value = self.search_form.cleaned_data['search']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class CreateTopicView(LoginRequiredMixin, CreateView):
    model = Topics
    template_name = 'Topics/topic_create.html'
    form_class = TopicForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:home')
