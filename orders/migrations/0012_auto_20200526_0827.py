# Generated by Django 3.0.6 on 2020-05-26 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200526_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2020, 5, 26)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userorder',
            name='totalPriceOrder',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
