# Generated by Django 4.1.6 on 2023-02-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0005_alter_chairman_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/chairman-default.png', upload_to='media/upload'),
        ),
    ]