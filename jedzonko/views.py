from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import *


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)


def recipes(request):
    return render(request, "recipe/list/app-recipes.html")
