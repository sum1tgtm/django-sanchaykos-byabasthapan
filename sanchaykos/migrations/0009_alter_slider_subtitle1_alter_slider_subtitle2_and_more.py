# Generated by Django 4.0.6 on 2022-08-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0008_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='subtitle1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='subtitle2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='subtitle3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title3',
            field=models.CharField(max_length=50),
        ),
    ]
