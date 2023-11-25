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

            # Send confirmation email to the user
            user_subject = 'Subscription Successful'
            user_message = 'Thank you for subscribing to our newsletter. You will receive updates and confirmations via email.'
            user_from_email = settings.DEFAULT_FROM_EMAIL
            user_recipient_list = [instance.email]

            send_mail(user_subject, user_message, user_from_email, user_recipient_list)

            # Send notification email to 'bluepulseband@example.com'
            admin_subject = 'New Newsletter Subscriber'
            admin_message = f'A new subscriber with email {instance.email} has joined the newsletter.'
            admin_from_email = settings.DEFAULT_FROM_EMAIL
            admin_recipient_list = ['bluepulseband@example.com']

            send_mail(admin_subject, admin_message, admin_from_email, admin_recipient_list)

            success_message = f"You have successfully subscribed to the newsletter. Confirmation email has been sent to {instance.email}."
            messages.success(request, success_message)

            return redirect("subscribe_success")

        return render(request, self.template_name, {"form": form})

class SubscribeSuccessView(View):
    template_name = "newsletter/subscribe_success.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
