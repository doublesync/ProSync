# Description: A view that renders the about page.
from django.shortcuts import render

# A function-based view that renders the about page
def about(request):
    return render(request, "core/about.html")
