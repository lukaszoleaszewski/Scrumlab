from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import *


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)


def recipes(request):
    return render(request, "app-recipes.html")

def dashboard(request):
    recipes = Recipe.objects.count()
    return render(request, "dashboard.html", context={"recipes": recipes,})