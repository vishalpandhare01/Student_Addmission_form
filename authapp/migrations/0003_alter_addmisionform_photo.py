# Generated by Django 3.2.12 on 2022-05-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_addmisionform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmisionform',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
