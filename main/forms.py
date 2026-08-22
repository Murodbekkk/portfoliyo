from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ismingiz", "class": "field", "autocomplete": "name"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "email@manzil.com", "class": "field", "autocomplete": "email"
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "Mavzu (ixtiyoriy)", "class": "field"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Xabaringizni shu yerga yozing...", "class": "field", "rows": 5
            }),
        }
