# Generated by Django 3.0.7 on 2020-06-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(max_length=15),
        ),
    ]