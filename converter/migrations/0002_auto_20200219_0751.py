# Generated by Django 3.0.3 on 2020-02-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converter',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
