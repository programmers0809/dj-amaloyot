from django.urls import path
from .views import HomeView, ContactView, NewsDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('news-detail/', NewsDetailView.as_view(), name='news_detail_page'),
]
