from django.db import models

# Create your models here.

class Ingredient_name(models.Model):
    ingredient_name_id = models.AutoField(primary_key = True)
    ingredient_name = models.CharField(max_length=64,verbose_name="성분 이름")

    def __str__(self):
        return self.ingredient_name

    class Meta():
        db_table = 'ingredient_name'
        verbose_name = '성분 이름'
        verbose_name_plural = '성분 이름'

class Ingredient_class(models.Model):
    ingredient_class_id = models.AutoField(primary_key = True)
    ingredient_class_name = models.CharField(max_length=64, verbose_name="성분 분류")

    def __str__(self):
        return self.ingredient_name

    class Meta():
        db_table = 'ingredient_class'
        verbose_name = '성분 분류'
        verbose_name_plural = '성분 분류'
        
class Ingredient_unit(models.Model):
    ingredient_unit_id = models.AutoField(primary_key = True, verbose_name='성분 단위')
    ingredient_unit_name = models.CharField(max_length=16, verbose_name="성분 단위")
    
    def __str__(self):
        return self.ingredient_unit_name
        
    class Meta():
        db_table = 'ingredient_unit'
        verbose_name = '성분 단위'
        verbose_name_plural = '성분 단위'
        
class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key = True)
    ingredient_name_id = models.ForeignKey(Ingredient_name, default='null', on_delete = models.CASCADE, verbose_name="성분 이름")
    ingredient_class_id = models.ForeignKey(Ingredient_class, default='null', on_delete = models.PROTECT, verbose_name="성분 분류")
    ingredient_detail_content = models.TextField(blank=True, verbose_name = "성분상세내용")
    ingredient_volume = models.PositiveIntegerField(default=0, verbose_name="성분 함량")
    ingredient_unit_id = models.ForeignKey(Ingredient_unit, default='null', on_delete=models.PROTECT, verbose_name="성분 단위")
    
    def __str__(self):
        return self.ingredient_name_id.ingredient_name +" "+ str(self.ingredient_volume) + self.ingredient_unit_id.ingredient_unit_name
        
    class Meta():
        db_table = 'ingredient'
        verbose_name = '성분'
        verbose_name_plural = '성분'
