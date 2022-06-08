from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .token import account_activation_token

def activation_email(user, current_site, receiver):
    subject = render_to_string('django_registration/activation_email_subject.txt')
    
    message = render_to_string('django_regsitration/activation_email_body.txt', {
                'user':user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user)
            })
    message_html = render_to_string('django_regsitration/activation_email_body.html', {
                'user':user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user)
            })
    mail = EmailMultiAlternatives(subject, message, to=[receiver])
    mail.attach_alternative(message_html,'text/html')
    mail.send()