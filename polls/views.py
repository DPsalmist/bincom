from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Sum
from django.contrib import messages
from .forms import PollForm
from django.db.models import Q
from .models import *

# Create your views here.
class HomeView(TemplateView):
    template_name = 'polls/index.html'

class SearchResultsView(ListView):
    model = POLLING_UNIT
    template_name = 'polls/search_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = POLLING_UNIT.objects.filter(
            Q(poll_unit_id__icontains=query)
        )
        return object_list

def createPoll(request):
	pu_results = POLLING_UNIT.objects.all()
	form = PollForm()

	if request.method == 'POST':
		form = PollForm(request.POST)
		if form.is_valid():
			form.save()
		messages.success(request, 'New Poll Unit was created successfully!')
		return redirect('/')
	else:
		form = PollForm()
	context = {'pu_results':pu_results, 'form':form,}
	return render(request, 'polls/create_new_pu.html', context)

def totalResults(request):
	pu_results = POLLING_UNIT.objects.all()
	announced_results = ANNOUNCED_PU_RESULTS.objects.all()
	announced_results_count = ANNOUNCED_PU_RESULTS.objects.all().count()
	total_announced_results = ANNOUNCED_PU_RESULTS.objects.aggregate(Sum('party_score'))

	context = {
		'pu_results':pu_results,
		'announced_results':announced_results,
		'total_announced_results':total_announced_results,
		'announced_results_count':announced_results_count,
	}
	return render(request, 'polls/announced_pu_results.html', context)

