from django.db import models

# Create your models here.

class Effect(models.Model):
    effect_id = models.AutoField(primary_key=True)
    effect_name = models.CharField(max_length=32, verbose_name='약 효능')
    
    def __str__(self):
        return self.effect_name
    
    class Meta():
        db_table = 'effect'
        verbose_name = '약 효능'
        verbose_name_plural = '약 효능'