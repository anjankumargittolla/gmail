# Generated by Django 3.2.3 on 2021-06-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mails',
            name='is_trash',
            field=models.BooleanField(default=False),
        ),
    ]