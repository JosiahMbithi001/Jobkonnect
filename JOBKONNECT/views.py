from django.shortcuts import render
def index(request):
    """
    Returns Default Homepage
    """
    return render(request, "templates/layout.html")
