# Generated by Django 3.1.5 on 2021-01-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orderupdate',
            name='update_desc',
            field=models.CharField(max_length=5000),
        ),
    ]
