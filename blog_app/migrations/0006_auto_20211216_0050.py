# Generated by Django 3.0.7 on 2021-12-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20211215_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DateTime Updated'),
        ),
    ]
