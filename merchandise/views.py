from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import MerchandiseMod
from django.views.generic.detail import DetailView


class AllMerchView(TemplateView):
    """
    Gets All Merchandise
    """
    model = MerchandiseMod
    template_name = 'merchandise/all_merch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_merch'] = MerchandiseMod.objects.all()
        return context


class merchandiseDetailView(DetailView):
    model = MerchandiseMod
    template_name = 'merchandise/merch_item.html'
    context_object_name = 'merch_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['merch_item'] = self.object
        return context

