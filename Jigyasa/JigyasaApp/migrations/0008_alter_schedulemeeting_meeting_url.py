# Generated by Django 3.2.7 on 2021-11-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JigyasaApp', '0007_auto_20211106_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulemeeting',
            name='meeting_url',
            field=models.CharField(default='', max_length=6000),
        ),
    ]
