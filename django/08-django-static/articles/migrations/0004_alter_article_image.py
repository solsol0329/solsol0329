# Generated by Django 4.2.5 on 2023-09-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_alter_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(blank=True, upload_to="%Y/%m/%d/"),
        ),
    ]
