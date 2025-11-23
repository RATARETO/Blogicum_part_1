from django.shortcuts import render
""" Модуль для отображения страниц через header, информации о сайте"""


def about(request):
    """Функция отображения для страницы about в header"""
    return render(request, 'posts/about.html')


def rules(request):
    """Функция отображения для страницы rules в header"""
    return render(request, 'posts/rules.html')
