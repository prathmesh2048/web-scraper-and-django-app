from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        # below line is used to display the email-address
        #print(form.cleaned_data['email'])
        name = form.cleaned_data['name']
        subject = 'Message from mysite.com'
        comment = form.cleaned_data['comment']
        message = '%s %s' % (comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(
            subject,
            message,
            emailFrom,
            emailTo,
            fail_silently=True,
        )
        title = 'Thanks!'
        confirm_message = 'Thanks for the message. we will get right back to you'
        form = None

    contex = {'title': title, 'form': form, 'confirm_message': confirm_message, }

    template = 'contact.html'
    return render(request, template, contex)