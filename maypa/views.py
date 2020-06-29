from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.postgres import *
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .filters import *
from django.http import HttpResponse
from .utils import render_to_pdf
import datetime



def index(request):
	return render(request, 'index.html')
	
def displayClients(request):
	items = cliente.objects.all()

	context = {
		'items': items
	}

	return render(request, 'index.html', context)

searchTerms = ""

def search(request):

	print(request.method == 'POST' )
	if request.method == 'POST':
		queryRequested = request.POST['content']
		if queryRequested:
			query = cliente.objects.filter(Q(NOMBRE__icontains = queryRequested) | Q(DIRECCION_FISICA__icontains = queryRequested) | Q(CIUDAD__icontains = queryRequested) | Q(EMAIL__icontains = queryRequested))
			if query:

				return render(request, 'search.html', {'sr': query, 'content': queryRequested})
			else:
				return render(request, 'search.html', {'sr':'No hay resultados'})
	else:
		return render('index')

"""class clientView(ListView):
	model = cliente
	template_name = 'search.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = clientFilter(self.request.GET, queryset = self.get_queryset())
		return context"""


def addClient(request):
	if request.method == 'POST':
		form = clienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = clienteForm()
		return render(request, 'addNew.html', {'form': form}) 

def editClient(request, pk):
	item = get_object_or_404(cliente, pk = pk)

	if request.method == 'POST':
		form = clienteForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = clienteForm(instance = item)
		return render(request, 'editClient.html', {'form': form})

def searchClient(request, newSearch):
	items = cliente.objects.filter(NOMBRE = newSearch)
	context = {
		'items': items
	}
	return render(request, 'showresults.html', context)
"""
def get(request):
	print(searchTerms)
	queryRequested = searchTerms
	query = cliente.objects.filter(Q(NOMBRE__icontains = queryRequested) | Q(DIRECCION_FISICA__icontains = queryRequested) | Q(CIUDAD__icontains = queryRequested) | Q(EMAIL__icontains = queryRequested))
	lista = {}
	if query:
		for item in query:
			lista[item.IDCLIENTE] = ({item.IDCLIENTE, item.NOMBRE, item.DIRECCION_FISICA, item.EMAIL})
		print(lista)
		pdf = render_to_pdf('invoice.html', lista)
		return HttpResponse(pdf, content_type='application/pdf')
	else:
		return render(request, 'search.html', {'sr':'No hay resultados'})"""