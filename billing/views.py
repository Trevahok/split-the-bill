from django.shortcuts import render
from .models import Debt
from django.contrib.auth.models import User
from .forms import DebtForm

# Create your views here.
def home(request):
    debt_form = DebtForm(request.POST or None)
    debt=Debt.objects.all()
    context={
            'form':debt_form,
            'debts':debt,
            }
    if request.method=='POST':
        d = Debt.objects.get_or_create(from_user=User.objects.get(id =request.POST['from_user']) , to_user=User.objects.get(id =request.POST['to_user']))
        d[0].amount+=int(request.POST['amount'])
        d[0].save()
    return render(request,'debt.html', context)


