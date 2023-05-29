from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    """Where Users will display their Certificates"""

    class Meta:
        """Certificates Metadata"""
        model = Certificate
        fields = '__all__'
