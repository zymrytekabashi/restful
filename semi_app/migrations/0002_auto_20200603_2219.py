# Generated by Django 2.2 on 2020-06-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
