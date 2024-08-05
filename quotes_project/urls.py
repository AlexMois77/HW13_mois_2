from django.contrib import admin
from django.urls import path, include

from quotes.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("quotes/", include("quotes.urls")),
    path("", HomeView.as_view(), name="home"),
]
