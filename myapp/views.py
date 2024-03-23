from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, "index.html", context)

# def home(request):
#     context = {}
#     return render(request, "contact.html", context)

# def home(request):
#     context = {}
#     return render(request, "shope-detail.html", context)

# def home(request):
#     context = {}
#     return render(request, "hope.html", context)

# def home(request):
#     context = {}
#     return render(request, "testimonial.html", context)
# def home(request):
#     context = {}
#     return render(request, "cart.html", context)

# def home(request):
#     context = {}
#     return render(request, "404.html", context)