from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    now = datetime.now()
    return render(
        request,
        "index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Hello Everyone",
            'message' : "This is my data! ",
            'content': "on " + now.strftime("%A, %d %B, %Y at %X")
        })

# Create your views here.
