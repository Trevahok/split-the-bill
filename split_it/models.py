from django.db import models 
from django.contib.auth.models import User

class BillList(models.Model):
    user =models.OneToOneField(User, one_delete=models.CASCADE)
    def __str__(self):
        self.user.username
