from django.shortcuts import render
from .models import Debt
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
        d = Debt.objects.get(from_user=request.POST['from_user'] , to_user=request.POST['to_user'])
        d.amount+=int(request.POST['amount'])
        d.save()
    return render(request,'debt.html', context)


