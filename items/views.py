from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    items = models.StoreItem.objects.all()
    if request.method == "POST":
        search = request.POST.get("search")

        return render(request, "search_result.html", context={"search": search, "item": items})
    return render(request, "home.html", context={"items": items})


def item_detail(request, pk):
    item = models.StoreItem.objects.get(pk=pk)

    return render(request, "item_details.html", context={"item": item})
