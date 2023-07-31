from django.contrib.auth.models import User
from django.db import models


class UserTutorialPurchased(models.Model):
    """
    This model represents the users who have purchased a tutorial.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey('Tutorial', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tutorial}"

    class Meta:
        unique_together = ['user', 'tutorial']


class Trainer(models.Model):
    """
    This model represents trainers.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email

    @property
    def tutorials(self):
        return self.tutorial_set.all()


class Category(models.Model):
    """
    This model represents categories of tutorials.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Tutorial(models.Model):
    """
    This model represents a tutorial.
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description_long = models.TextField()
    link_url = models.URLField()
    content = models.TextField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
