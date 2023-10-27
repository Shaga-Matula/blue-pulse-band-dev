from django.shortcuts import render, get_object_or_404
from .models import MerchandiseMod
from django.views.generic import TemplateView, UpdateView, View, ListView


def product_detail(request, pk):
    product = get_object_or_404(MerchandiseMod, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


class MerchandiseView(TemplateView):
    model = MerchandiseMod
    template_name = 'merch_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_goods'] = MerchandiseMod.objects.all()
        return context
