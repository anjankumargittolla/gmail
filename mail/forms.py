from django.forms import ModelForm

from .models import Mails


class MailsForm(ModelForm):
    """Modelform for Mails"""

    class Meta:
        model = Mails
        fields = ['receiver', 'subject', 'body']
