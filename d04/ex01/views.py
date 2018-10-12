from django.shortcuts import render
from ex01.models import Article

# Create your views here.
def django_page(request):

    django_article = Article()
    django_article.page_title = "Ex01 : Django, framework web."
    django_article.css_style = "style1"
    django_article.content = """
hello there
    """

    return render(request, 'ex01/base.html', {'article': django_article})


def affichage_page(request):

    affichage_article = Article()
    affichage_article.page_title = "Ex01 : Processus d’affichage d’une page statique."
    affichage_article.css_style = "style1"
    affichage_article.content = """
general kenobi
    """
    return render(request, 'ex01/base.html', {'article': affichage_article})


def templates_page(request):

    templates_article = Article()
    templates_article.page_title = "Ex01 : Moteur de template"
    templates_article.css_style = "style2"
    templates_article.content = """
you are a bold one
    """
    return render(request, 'ex01/base.html', {'article': templates_article})
