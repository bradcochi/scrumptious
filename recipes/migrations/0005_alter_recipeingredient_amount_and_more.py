# Generated by Django 4.2 on 2023-04-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipeingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='food_item',
            field=models.TextField(max_length=50),
        ),
    ]
