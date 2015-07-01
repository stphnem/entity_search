from django.shortcuts import render
from .forms import InputForm
import parse

# Create your views here.
entities = parse.import_entities()

def home(request):
	form = InputForm(request.POST or None)

	if form.is_valid():
		data = parse.highlight_links(form.cleaned_data['textInput'], entities)
		context = {
			'form': form,
			'data': parse.highlight_links(form.cleaned_data['textInput'], entities)
		}
	else:
		context = {
			'form': form,
		}

	template = 'home.html'
	return render(request, template, context)