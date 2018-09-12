from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Debt(models.Model):
    from_user=models.OneToOneField(User,on_delete=models.PROTECT,related_name='from_user')
    to_user= models.OneToOneField(User,on_delete=models.PROTECT,related_name='to_user')
    amount=models.SmallIntegerField(default=0)
    def __str__(self):
        return self.from_user.username+' owes '+self.to_user.username+' '+str(self.amount)
