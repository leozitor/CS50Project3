# Generated by Django 3.0.6 on 2020-05-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200526_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='totalPriceOrder',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
