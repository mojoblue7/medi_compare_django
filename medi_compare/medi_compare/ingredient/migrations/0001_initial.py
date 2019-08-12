# Generated by Django 2.2.4 on 2019-08-12 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient_class',
            fields=[
                ('ingredient_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_class_name', models.CharField(max_length=64, verbose_name='성분 분류')),
            ],
            options={
                'verbose_name': '성분 분류',
                'verbose_name_plural': '성분 분류',
                'db_table': 'ingredient_class',
            },
        ),
        migrations.CreateModel(
            name='Ingredient_name',
            fields=[
                ('ingredient_name_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=64, verbose_name='성분 이름')),
            ],
            options={
                'verbose_name': '성분 이름',
                'verbose_name_plural': '성분 이름',
                'db_table': 'ingredient_name',
            },
        ),
        migrations.CreateModel(
            name='Ingredient_unit',
            fields=[
                ('ingredient_unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_unit_name', models.CharField(max_length=16, verbose_name='성분 단위')),
            ],
            options={
                'verbose_name': '성분 단위',
                'verbose_name_plural': '성분 단위',
                'db_table': 'ingredient_unit',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_detail_content', models.TextField(blank=True, verbose_name='성분상세내용')),
                ('ingredient_volume', models.PositiveIntegerField(default=0, verbose_name='성분함량')),
                ('ingredient_class_id', models.ForeignKey(default='null', on_delete=django.db.models.deletion.PROTECT, to='ingredient.Ingredient_class')),
                ('ingredient_name_id', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='ingredient.Ingredient_name')),
                ('ingredient_unit_id', models.ForeignKey(default='null', on_delete=django.db.models.deletion.PROTECT, to='ingredient.Ingredient_unit')),
            ],
            options={
                'verbose_name': '성분',
                'verbose_name_plural': '성분',
                'db_table': 'ingredient',
            },
        ),
    ]
