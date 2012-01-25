from django.utils.translation import ugettext_lazy as _
from newsletter.models import NewsletterSubscription

from django import forms

class NewsletterForm(forms.Form):
    email = forms.EmailField(label=_("E-mail"), required=True, max_length=75,
        help_text=_("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages={ 'invalid': _("Email may contain only letters, numbers and characters @/./+/-/_. 30 characters or fewer.") })

    def clean_email(self):
        """
        Validates that a user exists with the given e-mail address.
        """
        email = self.cleaned_data["email"]

        return email
