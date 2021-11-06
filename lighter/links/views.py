from django.shortcuts import render

from .models import LinkPage

# Create your views here.
def links_index(request):
    return render(request, 'links/index.html', {'link_pages_list': LinkPage.objects.all()})
