# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from newsletter.models import NewsletterSubscription
from newsletter.forms import NewsletterForm

def send_mass_email(sender, to=None, bcc=None, subject=None, txt=None, html=None, attachment=None):
    """
    We always send in html and txt form.
    
    sender example: 'Sender Name <sender@internet.com>'
    receiver: ['email-1@email.net', ['email-2@email.net', ...]
    """

    message = EmailMultiAlternatives(subject, txt, sender, to, bcc, headers={'Reply-To': sender})
    message.attach_alternative(html, "text/html")
    message.content_subtype = "html"
    message.send()

def try_to_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                newsletter_subscription = NewsletterSubscription.objects.get(email=request.POST['email'])
            except NewsletterSubscription.DoesNotExist:
                newsletter_subscription = NewsletterSubscription(email=request.POST['email'], subscribed=False)
                newsletter_subscription.save()
                newsletter_subscription.set_token()

            subscribe_url = settings.SUBSCRIBE_URL % (settings.SITE_URL, newsletter_subscription.token)

            file = open(settings.TEMPLATE_DIRS[0] + "/newsletter/subscribe_send_token_" + translation.get_language() + ".txt", "r")
            message_txt = file.read()
            file.close()
            message_txt = message_txt.decode("utf-8")
            message_txt = message_txt % (subscribe_url)

            file = open(settings.TEMPLATE_DIRS[0] + "/newsletter/subscribe_send_token_" + translation.get_language() + ".html", "r")
            message_html = file.read()
            file.close()
            message_html = message_html.decode("utf-8")
            message_html = message_html % (subscribe_url, subscribe_url)
            
            print subscribe_url

            subject = "%s %s" % (settings.EMAIL_SUBJECT_PREFIX, unicode(_(u"newsletter subscription")))

            send_mass_email(settings.EMAIL_FROM, [request.POST['email']], None, subject, message_txt, message_html)

            return render_to_response('newsletter/subscription_token_sent_' + translation.get_language() + '.html', { 'SITE_URL': settings.SITE_URL }, context_instance=RequestContext(request))
    else:
        form = NewsletterForm()

    user = request.user

    if user and user.is_authenticated():
        try:
            newsletter_subscription = NewsletterSubscription.objects.get(email=user.email)
            if newsletter_subscription.subscribed == False:
                newsletter_subscription.subscribed = True
                newsletter_subscription.save()
                return render_to_response('newsletter/successfully_subscribed_' + translation.get_language() + '.html', { 'token': newsletter_subscription.token }, context_instance=RequestContext(request))
            else:
                return render_to_response('newsletter/already_subscribed_' + translation.get_language() + '.html', { 'subscription': newsletter_subscription, 'SITE_URL': settings.SITE_URL }, context_instance=RequestContext(request))

        except NewsletterSubscription.DoesNotExist:
            newsletter_subscription = NewsletterSubscription(email=request.POST['email'], subscribed=True)
            newsletter_subscription.save()
            newsletter_subscription.set_token()

    return render_to_response('newsletter/subscribe_' + translation.get_language() + '.html', { 'form': form, 'SITE_URL': settings.SITE_URL }, context_instance=RequestContext(request))

def try_to_unsubscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                newsletter_subscription = NewsletterSubscription.objects.get(email=request.POST['email'])
            except NewsletterSubscription.DoesNotExist:
                return render_to_response('newsletter/no_subscription_' + translation.get_language() + '.html', context_instance=RequestContext(request))

            unsubscribe_url = settings.UNSUBSCRIBE_URL % (settings.SITE_URL, newsletter_subscription.token)

            file = open(settings.TEMPLATE_DIRS[0] + "/newsletter/unsubscribe_send_token_" + translation.get_language() + ".txt", "r")
            message_txt = file.read()
            file.close()
            message_txt = message_txt.decode("utf-8")
            message_txt = message_txt % (unsubscribe_url)

            file = open(settings.TEMPLATE_DIRS[0] + "/newsletter/unsubscribe_send_token_" + translation.get_language() + ".html", "r")
            message_html = file.read()
            file.close()
            message_html = message_html.decode("utf-8")
            message_html = message_html % (unsubscribe_url, unsubscribe_url)

            subject = "%s %s" % (settings.EMAIL_SUBJECT_PREFIX, unicode(_(u"newsletter unsubscription")))

            send_mass_email(settings.EMAIL_FROM, [request.POST['email']], None, subject, message_txt, message_html)

            return render_to_response('newsletter/unsubscription_token_sent_' + translation.get_language() + '.html', context_instance=RequestContext(request))
    else:
        form = NewsletterForm()

    user = request.user

    if user and user.is_authenticated():
        try:
            subscription = NewsletterSubscription.objects.get(email=user.email)
            if subscription.subscribed == False:
                return render_to_response('newsletter/already_unsubscribed_' + translation.get_language() + '.html', { 'subscription': subscription }, context_instance=RequestContext(request))
        except NewsletterSubscription.DoesNotExist:
            pass

    return render_to_response('newsletter/unsubscribe_' + translation.get_language() + '.html', { 'form': form }, context_instance=RequestContext(request))

def subscribe(request, key, subscribed):
    if request.method == 'GET':
        try:
            newsletter_subscription = NewsletterSubscription.objects.get(token=key)
            newsletter_subscription.subscribed = subscribed
            newsletter_subscription.save()
        except NewsletterSubscription.DoesNotExist:
            return render_to_response('newsletter/no_subscription_' + translation.get_language() + '.html', context_instance=RequestContext(request))

        if subscribed == True:
            return render_to_response('newsletter/successfully_subscribed_' + translation.get_language() + '.html', { 'token': newsletter_subscription.token }, context_instance=RequestContext(request))
        else:
            return render_to_response('newsletter/successfully_unsubscribed_' + translation.get_language() + '.html', { 'token': newsletter_subscription.token }, context_instance=RequestContext(request))
