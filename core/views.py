from django.shortcuts import render

# Interface frontend as index.html
def front(request):
    context = { }
    return render(request, "index.html", context)

