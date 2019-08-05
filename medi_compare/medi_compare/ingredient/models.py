from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=80 ,verbose_name="성분이름")
    ingredient_class = models.CharField(max_length=50, verbose_name="성분분류")
    detail_content = models.TextField(blank=True,
        verbose_name = "성분상세내용")
    
    def __str__(self):
        return self.ingredient_name.ingredient_name + " " + str(self.volume)
        
    class Meta:
        db_table = 'ingredient'
        verbose_name = '성분'
        verbose_name_plural = '성분'
