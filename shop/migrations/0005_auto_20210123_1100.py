# Generated by Django 3.1.5 on 2021-01-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210123_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='ok bro', max_length=500),
        ),
    ]