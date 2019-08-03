from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_name = models.ForeignKey('ingredient.IngredientName', on_delete=models.CASCADE,
                                        verbose_name = "성분이름")
    volume = models.IntegerField(default = 0, 
                                 verbose_name = "성분함량")
    detail_content = models.TextField(
        verbose_name = "성분상세내용")
    
    class Meta:
        verbose_name = '성분'
        verbose_name_plural = '성분'

    def __str__(self):
        return self.ingredien_name
    
class IngredientName(models.Model):
    ingredient_name = models.CharField(max_length = 100, primary_key = True)