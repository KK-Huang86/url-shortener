from url_shortner.models import Url
from django.forms import ModelForm
from django.forms.widgets import URLInput
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django import forms



class UrlForm(ModelForm):
  class Meta:
    model=Url
    fields=["original_url"]
    widget={
      "original_url":URLInput( attrs={"placeholder": "請輸入網址"})
    }
    labels={
       "original_url":"原始網址"
    }

  def clean_original_url(self):
    original_url=self.cleaned_data.get('original_url')
    validator = URLValidator()
    try:
        validator(original_url)
    except ValidationError:
        raise forms.ValidationError('請輸入有效的網址')
    return original_url




