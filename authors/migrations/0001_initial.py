# Generated by Django 4.1.2 on 2022-10-12 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('pic', models.ImageField(upload_to='uploads/')),
                ('bio', models.TextField(verbose_name='bio')),
                ('twitter', models.CharField(blank=True, max_length=40)),
                ('youtube', models.CharField(blank=True, max_length=40)),
                ('facebook', models.CharField(blank=True, max_length=40)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
