from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.ForeignKey('Ingredient_name', on_delete=models.CASCADE)
    ingredient_detail_content = models.TextField(blank=True, verbose_name = "성분상세내용")
    ingredient_volume = models.IntegerField(default=0, verbose_name="성분함량")
    ingredient_unit = models.ForeignKey('Ingredient_unit', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.ingredient_name.ingredient_name + " " + str(self.volume) + self.ingredient_unit
        
    class Meta():
        db_table = 'ingredient'
        verbose_name = '성분'
        verbose_name_plural = '성분'

class Ingredient_name(models.Model):
    ingredient_name = models.CharField(max_length=80 ,verbose_name="성분이름")
    ingredient_class = models.CharField(max_length=80, verbose_name="성분분류")

    def __str__(self):
        return self.ingredient_name    
    class Meta():
        db_table = 'ingredient_name'
        verbose_name = '성분이름'
        verbose_name_plural = '성분이름'
        
class Ingredient_unit(models.Model):
    ingredient_unit = models.CharField(max_length=10, verbose_name="성분단위")
    
    def __str__(self):
        return self.ingredient_unit 
    class Meta():
        db_table = 'ingredient_unit'
        verbose_name = '성분단위'
        verbose_name_plural = '성분단위'