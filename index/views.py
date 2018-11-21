from django.shortcuts import render, get_object_or_404
from .models import Code, Division

def index_page(request):
    codes = Code.objects.all()
    divisions = Division.objects.all()
    template = 'index/index_page.html'
    context = {'divisions': divisions}
    return render(request, template, context)
