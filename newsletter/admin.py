# -*- coding: utf-8 -*-
import datetime

from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from newsletter.models import Newsletter, NewsletterSubscription
from newsletter.views import send_mass_email

def send_emails(newsletter, emails):
    if settings.DEBUG == True:
        emails = [d[1] for d in settings.ADMINS]

    send_mass_email(settings.EMAIL_FROM, None, emails, newsletter.title, newsletter.txt, newsletter.html)

    if settings.DEBUG != True:
        newsletter.datetime_sent = datetime.datetime.now()
        newsletter.sent_to = ';'.join(emails)
        newsletter.save()

def send_newsletter(modeladmin, request, queryset):
    for q in queryset:
        newsletter_subscriptions = NewsletterSubscription.objects.filter(subscribed=True)
        emails = [ns.email for ns in newsletter_subscriptions]
        send_emails(q, emails)

send_newsletter.short_description = _(u"Send newsletter")

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['title', 'txt', 'html', 'datetime_sent']
    ordering = ['-datetime_sent']
    actions = [send_newsletter]

admin.site.register([Newsletter], NewsletterAdmin)
admin.site.register([NewsletterSubscription])

