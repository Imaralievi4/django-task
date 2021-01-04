from django.db import models
from django.shortcuts import reverse
from django.conf import settings 
from django.contrib.auth import get_user_model
# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('detail_list', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('update_list', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('delete_list', kwargs={'slug': self.slug})

