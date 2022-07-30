from django.forms  import ModelForm
from . models import Details
class Df(ModelForm):
    class Meta:
        model=Details
        fields ='__all__'