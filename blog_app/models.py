from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime

blog_status = (
    ('Pending for review','Pending for review'),
    ('Revision requested','Revision requested'),
    ('Shortlisted','Shortlisted'),
    ('Rejected','Rejected'),
    ('Draft', 'Draft'),
)

updated_by = (
    ('Aryan','Aryan'),
    ('Chirag','Chirag'),
)

# Create your models here.
class Blog(models.Model):
    blog_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Username")
    article_name = models.CharField(max_length=10000, default="")
    date_created = models.DateTimeField(null=True, blank=True, verbose_name="DateTime Created")
    date_updated = models.DateTimeField(verbose_name="DateTime Updated", null=True, blank=True)
    updated_by = models.CharField(choices=updated_by, max_length=100, default='Aryan')
    blog_status = models.CharField(choices=blog_status, max_length=100, default='Draft', verbose_name="Current Status")
    google_doc_link = models.URLField(max_length=500, null=False, blank=False, verbose_name="Google Doc Link")
    review_by_admin = models.CharField(max_length=10000, default="", verbose_name="Your Review")
    isPaid = models.BooleanField(default=False, verbose_name="Eligible for payment or not")
    amount_to_pay = models.IntegerField(default=0, verbose_name="Amount to Pay")
    

    def __str__(self):
        return self.user.username