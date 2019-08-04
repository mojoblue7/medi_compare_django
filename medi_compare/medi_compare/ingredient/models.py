from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.ForeignKey('IngredientName', on_delete=models.CASCADE, verbose_name = "성분이름")
    volume = models.IntegerField(default = 0, 
                                 verbose_name = "성분함량")
    detail_content = models.TextField(blank=True,
        verbose_name = "성분상세내용")
    
    def __str__(self):
        return self.ingredient_name.ingredient_name + " " + str(self.volume)
        
    class Meta:
        db_table = 'ingredient'
        verbose_name = '성분'
        verbose_name_plural = '성분'


class IngredientName(models.Model):
    ingredient_name = models.CharField(max_length = 100, primary_key = True)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        db_table = 'ingredient_name'
        verbose_name = '성분이름'
        verbose_name_plural = '성분이름'

