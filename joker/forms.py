from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name", "email_addres", "content"]
    
    def clean(self):
        super(ContactForm, self).clean()
        
    
        full_name = self.cleaned_data.get('full_name')
        content = self.cleaned_data.get('content')

      
        if full_name:
            if len(full_name) < 3:
                raise forms.ValidationError("Full name must be at least 3 characters")
        else:
            self._errors['full_name'] = self.error_class([
                    'Full name is required'])

        if not content:
            self._errors['content'] = self.error_class([
                    'Content is required'])
        
        return self.cleaned_data
