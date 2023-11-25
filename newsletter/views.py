from django.core.mail import send_mail, settings
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages 
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
            instance = form.save(commit=False)  # Do not save to the database yet
            
            instance.save()  # Save to the database now
            # Send email to 'me@me.com'
            subject = 'Subscription Successful'
            message = f'A new subscriber with email {instance.email} has subscribed to the newsletter.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['bluepulseband@gmail.com']

            send_mail(subject, message, from_email, recipient_list)

            success_message = "You have successfully subscribed to the newsletter. An email has been sent to 'me@me.com'."
            messages.success(request, success_message)

            return redirect("subscribe_success")

        return render(request, self.template_name, {"form": form})

class SubscribeSuccessView(View):
    template_name = "newsletter/subscribe_success.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
