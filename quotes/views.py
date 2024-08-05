from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator

from quotes.forms import TagForm, AuthorForm, QuoteForm
from quotes.models import Quote, Authors, Tag


# Create your views here.


class HomeView(ListView):
    model = Quote
    template_name = "home.html"
    context_object_name = "quotes"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quotes"] = context["page_obj"]
        return context


class AuthorDetailView(DetailView):
    model = Authors
    template_name = "quotes/author_detail.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quotes"] = Quote.objects.filter(author=self.object)
        return context


class AddTagView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Tag
    template_name = "quotes/add_tag.html"
    success_url = reverse_lazy("home")
    form_class = TagForm


class AddAuthorView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Authors
    template_name = "quotes/add_author.html"
    success_url = reverse_lazy("home")
    form_class = AuthorForm


class AddQuoteView(LoginRequiredMixin, CreateView):
    login_url = "/users/login/"
    model = Authors
    template_name = "quotes/add_quote.html"
    success_url = reverse_lazy("home")
    form_class = QuoteForm


class TagQuoteListView(ListView):
    model = Quote
    template_name = "quotes/tag_quotes.html"
    context_object_name = "quotes"

    def get_queryset(self):
        tag_id = self.kwargs["pk"]
        return Quote.objects.filter(tags__id=tag_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs["pk"]
        context["tag"] = Tag.objects.get(id=tag_id)
        return context
