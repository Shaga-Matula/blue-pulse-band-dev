from django.shortcuts import render, get_object_or_404
from .models import MerchandiseMod

def product_detail(request, pk):
    product = get_object_or_404(MerchandiseMod, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


