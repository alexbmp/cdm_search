from django.shortcuts import render
from django.http import HttpResponse
from index.models import Code
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search_form(request):
    if request.method == "GET":
        template = 'meas_lab/search_form.html'
        return render(request, template)

    return HttpResponse('Search a valid manner.')

def search(request):
    template = "meas_lab/search.html"
    query = request.GET.get('q')
    if query:
        codes = Code.objects.filter(Q(division__name="Measurement lab")
            & (Q(source_id__icontains=query)
            | Q(source_name__icontains=query)
            | Q(target_name__icontains=query)))
        if codes:
            context = {'codes': codes}
            return render(request, template, context)
        else:
            return HttpResponse('No results found.')
    else:
        return HttpResponse("You should at least search for something.")

    #paginator = Paginator(object_list, 10)
    #page = request.GET.get('page')
    #try:
    #    items = paginator.page(page)
    #except PageNotAnInteger:
    #    items = paginator.page(1)
    #except EmptyPage:
    #    items = paginator.page(paginator.num_pages)

    #context = {
    #    'items': items,
    #}
    """
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        codes = Code.object.filter(division__name="Measurement lab")
    else:
        return HttpResponse("Please submit a search term.")

    # division <- Division instance that has name as attribute
    template = 'meas_lab/search.html'
    context = {'codes': codes}
    return render(request, template, context)
"""
