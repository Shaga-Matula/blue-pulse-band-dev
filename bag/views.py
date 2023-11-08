from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from django.contrib import messages
from merchandise.models import MerchandiseMod

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = MerchandiseMod.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
        print(f"Size Mate: {size}") 
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Added another {product.name} to your bag boy,o')
            print("Another one")
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag big lad')
            print("This is a test message for views.py")

    request.session['bag'] = bag
    return redirect(redirect_url)


class AdjustBagView(View):
    def post(self, request, item_id):
        """Adjust the quantity of the specified product to the specified amount"""

        quantity = int(request.POST.get('quantity'))
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            if quantity > 0:
                if item_id in bag:
                    bag[item_id]['items_by_size'][size] = quantity
                else:
                    bag[item_id] = {
                        'items_by_size': {size: quantity}
                    }
            else:
                if item_id in bag and size in bag[item_id]['items_by_size']:
                    del bag[item_id]['items_by_size'][size]
                    if not bag[item_id]['items_by_size']:
                        bag.pop(item_id)
        else:
            if quantity > 0:
                bag[item_id] = quantity
            else:
                bag.pop(item_id)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


    

