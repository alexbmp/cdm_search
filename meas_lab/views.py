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
    page = request.GET.get('page')
    if not page:
        page = 1
    if query:
        codes = Code.objects.filter(Q(division__name="Measurement lab")
            & (Q(source_id__icontains=query)
            | Q(source_name__icontains=query)
            | Q(target_name__icontains=query)))
        if codes:
            paginator = Paginator(codes, 10)
            codes = paginator.get_page(page)
            context = {'codes': codes, 'q': query}
            return render(request, template, context)
        else:
            context = {'message': 'No results found.'}
            return render(request, template, context)
    else:
        context = {'message': 'You should at least search for something.'}
        return render(request, template, context)

