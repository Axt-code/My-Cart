# Generated by Django 3.1.5 on 2021-01-23 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210123_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]