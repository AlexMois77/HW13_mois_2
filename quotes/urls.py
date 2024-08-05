from django.urls import path

from quotes.views import (
    AddTagView,
    AddAuthorView,
    AddQuoteView,
    HomeView,
    AuthorDetailView,
    TagQuoteListView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_tag/", AddTagView.as_view(), name="add_tag"),
    path("add_author/", AddAuthorView.as_view(), name="add_author"),
    path("add_quote/", AddQuoteView.as_view(), name="add_quote"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("tags/<int:pk>/", TagQuoteListView.as_view(), name="tag_quotes"),
]
