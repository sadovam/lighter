from django.shortcuts import render

from .models import LinkPage, LinkGroup


def links_index(request):
    return render(request, 'links/index.html', {'link_pages_list': LinkPage.objects.all()})


def page(request, page_id):
    return render(request, 'links/page.html', {'page': LinkPage.objects.get(pk=page_id)})
