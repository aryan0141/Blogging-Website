# Generated by Django 3.0.7 on 2021-12-15 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('article_name', models.CharField(default='', max_length=10000)),
                ('date_created', models.DateTimeField(verbose_name='DateTime Created')),
                ('date_updated', models.DateTimeField(verbose_name='DateTime Updated')),
                ('updated_by', models.CharField(choices=[('Aryan', 'Aryan'), ('Chirag', 'Chirag')], default='Aryan', max_length=100)),
                ('blog_status', models.CharField(choices=[('Pending for review', 'Pending for review'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected'), ('Draft', 'Draft')], default='Pending for review', max_length=100)),
                ('google_doc_link', models.URLField(max_length=500, verbose_name='Google Doc Link')),
                ('review_by_admin', models.CharField(default='', max_length=10000)),
                ('isPaid', models.BooleanField(default=False)),
                ('amount_to_pay', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
