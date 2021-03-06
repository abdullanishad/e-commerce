# Generated by Django 3.0.4 on 2020-06-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200613_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='productinstance',
            old_name='product',
            new_name='title',
        ),
    ]
