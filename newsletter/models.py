import string
from random import choice

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import transaction

def get_random_string(length=8, chars=string.letters + string.digits):
    return ''.join([choice(chars) for i in xrange(length)])

class NewsletterSubscription(models.Model):
    email = models.EmailField(_('Email'), blank=False, null=False, unique=True, db_index=True)
    token = models.CharField(_('Token for unsubscription'), max_length=15, blank=True, null=True, unique=True, db_index=True)
    subscribed = models.BooleanField(_('Subscribed or not'), blank=False, null=False)

    def __unicode__(self):
        return u'%s %s' % (self.email, self.subscribed)

    @transaction.autocommit
    def set_token(self):
        if self.token is None or self.token == '':
            token = None
            i = 0
            while token is None:
                if i == 100:
                    raise Exception("Too many times (100) generated random strings. WTF?")

                token = get_random_string(length=15)
                try:
                    newsletter_subscriptions = NewsletterSubscription.objects.get(token=token)
                    token = None
                except NewsletterSubscription.DoesNotExist:
                    self.token = token
                    self.save()

                i += 1

    def save(self, *args, **kwargs):
        super(NewsletterSubscription, self).save(*args, **kwargs)
        self.set_token()

class Newsletter(models.Model):
    title = models.CharField(_('Title of the newsletter'), max_length=255, blank=False, null=False)
    txt = models.TextField(_('Text version of email'), blank=True, null=True)
    html = models.TextField(_('HTML version of email'), blank=True, null=True)
    sent_to = models.TextField(_('Emails sent to'), help_text=_('Emails that have received newsletter'), blank=True, null=True, editable=False)
    datetime_sent = models.DateTimeField(_('Datetime mail sent'), blank=True, null=True, editable=False)

    __unicode__ = lambda self: u'%s %s' % (self.title, self.datetime_sent)
