# Generated by Django 3.2.12 on 2022-05-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_alter_addmisionform_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmisionform',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]