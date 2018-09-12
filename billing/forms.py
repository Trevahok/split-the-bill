from django.forms import ModelForm
from billing.models import Debt 

class DebtForm(ModelForm):
    class Meta:
        fields= '__all__'
        model =Debt
