from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import MerchandiseMod
from django.views.generic.detail import DetailView


class AllMerchView(TemplateView):
    """
    Gets All Merchandise
    """
    model = MerchandiseMod
    template_name = 'merchendise/all_merch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_merch'] = MerchandiseMod.objects.all()
        return context


# class MerchDetailView(TemplateView):
#
#     template_name = 'merchendise/detail_merch.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         merch = get_object_or_404(MerchandiseMod, pk=self.kwargs['pk'])
#         context['merch_id'] = merch
#         return context

#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         return render(request, self.template_name, context)


class MerchendiseDetailView(DetailView):
    model = MerchandiseMod
    template_name = 'merchendise/detail_merch.html'
    context_object_name = 'merchantobj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['merchantobj'] = self.object
        return context

