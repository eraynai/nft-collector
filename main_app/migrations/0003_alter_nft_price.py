# Generated by Django 3.2.4 on 2021-07-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='price',
            field=models.FloatField(),
        ),
    ]
