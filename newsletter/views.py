from django.shortcuts import redirect, render
from django.views import View

from .forms import SubscribeForm
from .models import NewsLetterMod


class SubscribeView(View):
    template_name = "newsletter/subscribe.html"

    def get(self, request, *args, **kwargs):
        form = SubscribeForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            # Need a success message here 
            return redirect("subscribe_success")

        return render(request, self.template_name, {"form": form})


class SubscribeSuccessView(View):
    template_name = "newsletter/subscribe_success.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
