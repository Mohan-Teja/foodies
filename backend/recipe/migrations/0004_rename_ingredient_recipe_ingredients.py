# Generated by Django 4.1.1 on 2022-10-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0003_recipe_ingredient"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe", old_name="ingredient", new_name="ingredients",
        ),
    ]
