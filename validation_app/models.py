from django.db import models
from datetime import datetime


class VideoGameManager(models.Manager):
    def basic_validator(self, postData):
        dia = datetime.now().strftime("%Y-%m-%d")
        print("dia")
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title cannot be less than 2 characters"
        if len(postData['company_name']) < 10:
            errors["company_name"] = "Company name cannot be less than 2 characters"
        if dia:
            errors["release_date"] = "Release Date cannot be empty"
        if len(postData['description']) < 5:
            errors["description"] = "Description cannot be less than 5 characters"
        return errors


class Video_Game(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    company = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = VideoGameManager()
