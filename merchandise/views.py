from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import MerchandiseMod
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.db.models import Q


class AllMerchView(TemplateView):
    template_name = 'merchandise/all_merch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q')

        if search_query:
            queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            all_merch = MerchandiseMod.objects.filter(queries)
            if all_merch:
                context['all_merch'] = all_merch
                messages.success(self.request, f"Search items results successfully retrieved for '{search_query}'")
            else:
                context['all_merch'] = []
                messages.warning(self.request, f"No items found for '{search_query}'")
        else:
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
