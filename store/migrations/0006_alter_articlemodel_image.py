# Generated by Django 5.1.2 on 2024-11-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_articlemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
    ]