from django.shortcuts import render

def index(request):
    """
    Returns Default Homepage
    """
    return render(request, "index.html")
