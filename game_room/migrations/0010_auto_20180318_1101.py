# Generated by Django 2.0.2 on 2018-03-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_room', '0009_applydetail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applydetail',
            name='id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='订单id'),
        ),
    ]
