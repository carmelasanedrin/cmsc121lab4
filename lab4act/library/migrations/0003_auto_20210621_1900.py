# Generated by Django 3.2.4 on 2021-06-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20210621_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
