# Generated by Django 2.0 on 2018-07-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotha_app', '0004_auto_20180725_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='ip_address',
            field=models.TextField(default='test ip'),
            preserve_default=False,
        ),
    ]