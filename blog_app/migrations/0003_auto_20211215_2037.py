# Generated by Django 3.0.7 on 2021-12-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20211215_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='DateTime Created'),
        ),
    ]
