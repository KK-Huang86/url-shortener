from url_shortner.models import Url
from django.forms import ModelForm
from django.forms.widgets import URLInput,CheckboxInput
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django import forms



class UrlForm(ModelForm):
  class Meta:
    model=Url
    fields=["original_url","is_active"]
    widgets={
      "original_url":URLInput( attrs={ "class":"input input-bordered w-full max-w-xs text-base" ,"placeholder": "請輸入或貼上完整的網址"}),
      "is_active":CheckboxInput(attrs={ "class":"checkbox" "input type=checkbox checked=checked" })
    }
    labels={
      "original_url":"連結",
      "is_active":"是否啟用短網址"
    }

  def clean_original_url(self):
    original_url=self.cleaned_data.get('original_url')
    validator = URLValidator()
    try:
        validator(original_url)
    except ValidationError:
        raise forms.ValidationError('請輸入有效的網址')
    return original_url




