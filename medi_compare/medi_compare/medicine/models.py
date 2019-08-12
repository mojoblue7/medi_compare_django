from django.db import models
from ingredient.models import Ingredient
from company.models import Company
# Create your models here.

class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key = True)
    medicine_name = models.ForeignKey('Medicine_name', on_delete=models.CASCADE)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    # effect_id = models.ForeignKey('Effect', on_delete=models.DO_NOTHING)
    # medicine_how_to_eat = models.
    
    
    def __str__(self):
        return self.company.company_name + self.medicine_name.medicine_name
    
    class Meta():
        db_table = 'medicine'
        verbose_name = '약 정보'
        verbose_name_plural = '약 정보'
        
class Medicine_name(models.Model):
    medicine_name_id = models.AutoField(primary_key = True)
    medicine_name = models.CharField(max_length=32, verbose_name='약 이름')
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table = 'medicine_name'
        verbose_name = '약 이름'
        verbose_name_plural = '약 이름'
        

