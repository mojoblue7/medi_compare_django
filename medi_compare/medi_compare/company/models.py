from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length=64, verbose_name='제약회사명')
    company_address = models.CharField(max_length=64, verbose_name='제약회사 주소', blank=True)
    company_phone_number = models.CharField(max_length=15, verbose_name='제약회사 전화번호', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table = 'company_name'
        verbose_name = '제약회사'
        verbose_name_plural = '제약회사'