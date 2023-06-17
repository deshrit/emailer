from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .forms import EmailerForm
from .tasks import mail_send

def index(request):
    form = EmailerForm()
    if request.method == "POST":
        form = EmailerForm(request.POST)
        if form.is_valid():
            mail_send.delay(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['receiver']],
                fail_silently=False
            )
            messages.add_message(
                request, 
                messages.SUCCESS, 
                "Email sent to queue sucesfully",
                fail_silently=True,
            )
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'emailer/index.html', context)