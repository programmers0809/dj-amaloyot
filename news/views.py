from django.shortcuts import render
from django.views import View
from .models import CategoryModel, NewsModel
from django.shortcuts import render, get_object_or_404
# from .models import News


class HomeView(View):
    def get(self, request):
        category_list = CategoryModel.objects.all()
        all_news_list = NewsModel.objects.all().order_by('-publish_time')  # 'manager' o'rniga 'objects' ishlatilmoqda
        uzb_news_list = NewsModel.objects.filter(category__name="O'zbekiston").order_by('-publish_time')[:6]  # 'all' chaqiruvini olib tashlang
        soport_news_list = NewsModel.objects.filter(category__name="Soort").order_by('-publish_time')[:6],
        jahon_news_list = NewsModel.objects.filter(category__name="Jahon").order_by('-publish_time')[:6],
        jamiyat_news_list=NewsModel.objects.filter(category__name="JAMIYAT").order_by('-publish_time')[:6],
        fan_tkink_news_list=NewsModel.objects.filter(category__name="Fan-txnika").order_by('-publish_time')[:6],
        context = {
            'category_list': category_list,
            'all_news_list': all_news_list,
            'uzb_news_list': uzb_news_list,
            'soport_news_list':soport_news_list,
            'jahon_news_list':jahon_news_list ,
            'jamiyat_news_list':jamiyat_news_list,
            'fan_tkink_news_list':fan_tkink_news_list
        }
        return render(request, 'news/home.html', context)


class ContactView(View):
    def get(self, request):
        context = {}  # Kerak bo'lsa, har qanday kontekst ma'lumotlarini qo'shing
        return render(request, 'news/contact.html', context)


class NewsDetailView(View):
    def get(self, request):
        context = {}  # Kerak bo'lsa, har qanday kontekst ma'lumotlarini qo'shing
        return render(request, 'news/news_detail.html', context)


def news_detail_page(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, 'news/news_detail_page.html', {'news': news})