# Generated by Django 3.0.4 on 2020-06-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]
