# Generated by Django 3.1 on 2020-08-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
