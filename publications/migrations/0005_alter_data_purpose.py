# Generated by Django 3.2.13 on 2022-06-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_alter_data_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='purpose',
            field=models.TextField(verbose_name='Zweck'),
        ),
    ]
