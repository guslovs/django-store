# Generated by Django 5.1.2 on 2024-11-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_articlemodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(upload_to='djangostoreimg'),
        ),
    ]
