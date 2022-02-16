from django.shortcuts import render
# Ahora heredaremos TemplateView en vez de View.
from django.views.generic import ListView, TemplateView
from web_cv import models

from django.utils.translation import gettext as _
from django.utils import translation


class Main_cv(TemplateView):
    template_name = "web_cv/main_cv.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estudios"] = list(models.Estudios.objects.all())
        context["trabajos"] = list(models.Trabajos.objects.all())

        return context
