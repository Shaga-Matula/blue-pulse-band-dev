from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .forms import MerchandiseForm
from .models import MerchandiseMod


class AllMerchView(TemplateView):
    template_name = "merchandise/all_merch.html"

    query = None
    categories = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get("q")
        category_name = self.request.GET.get("category")  # Get the 'category'
        all_merch = MerchandiseMod.objects.all()

        if category_name:
            # ForeignKey
            all_merch = all_merch.filter(category__name=category_name)

        if search_query:
            queries = Q(name__icontains=search_query) | Q(
                description__icontains=search_query
            )
            all_merch = all_merch.filter(queries)

        context["all_merch"] = all_merch

        if not all_merch:
            messages.warning(
                self.request, f"Sorry, no items retrieved for '{search_query}'"
            )

        return context


class MerchandiseDetailView(DetailView):
    """
    Render: an enlarged single item on click
    """

    model = MerchandiseMod
    template_name = "merchandise/merch_item.html"
    context_object_name = "merch_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["merch_item"] = self.object
        return context


@login_required
def add_merch(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store administrators can do that.")
        return redirect(reverse("home"))
    if request.method == "POST":
        form = MerchandiseForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("merch_item", args=[new_product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = MerchandiseForm()

    template = "merchandise/add_merch.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store administrators can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(MerchandiseMod, pk=product_id)
    if request.method == "POST":
        form = MerchandiseForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("merch_item", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = MerchandiseForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "merchandise/edit_merch.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store administrators can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(MerchandiseMod, pk=product_id)
    product.delete()
    messages.success(request, "Item deleted!")

    return redirect(reverse("all_merchandise"))
