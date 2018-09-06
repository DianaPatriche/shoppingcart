from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {'products': products }
    return render(request, 'list.html', context)


def product_detail(request):
    id = request.GET.get('id')
    produs = Product.objects.get(pk=int(id))
    print(produs.id)
    context = {'produs': produs}
    return render(request, 'produs.html', context)