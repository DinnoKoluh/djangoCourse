from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {
        'text': 'fuck me hello world',
        'number': 100,
    }
    return render(request, 'temp_app/index.html', context=context_dict)

def other(request):
    return render(request, 'temp_app/other.html')

def relative(request):
    return render(request, 'temp_app/relative_url_templates.html')
