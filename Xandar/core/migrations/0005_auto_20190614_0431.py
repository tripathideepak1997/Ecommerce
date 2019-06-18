# Generated by Django 2.1.7 on 2019-06-14 04:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190613_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsubcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='valid_till',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 4, 31, 8, 186039)),
        ),
    ]
