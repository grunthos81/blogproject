# Generated by Django 4.1.2 on 2022-10-13 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_last_edited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
        migrations.AlterField(
            model_name='article',
            name='last_edited',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 20, 33, 11, 787821)),
        ),
    ]
