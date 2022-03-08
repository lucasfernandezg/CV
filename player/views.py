from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.


from django.core.paginator import Paginator
from . models import Song


def Index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "player/index.html", context)
