# Generated by Django 4.1.1 on 2022-10-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0007_remove_recipe_recipe_likes_likedrecipes_recipe_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="recipe_photo1",
            field=models.ImageField(blank=True, null=True, upload_to="recipes/"),
        ),
        migrations.AddField(
            model_name="recipe",
            name="recipe_photo2",
            field=models.ImageField(blank=True, null=True, upload_to="recipes/"),
        ),
        migrations.AddField(
            model_name="recipe",
            name="recipe_photo3",
            field=models.ImageField(blank=True, null=True, upload_to="recipes/"),
        ),
    ]
