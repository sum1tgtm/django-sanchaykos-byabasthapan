# Generated by Django 4.0.6 on 2022-08-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanchaykos', '0004_alter_chairman_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='bigimage',
            field=models.ImageField(null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='chairman',
            name='image',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]
