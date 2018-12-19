from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# different type of membership options/packages
PACKAGES = (
    ('BAS', 'Basic'),
    ('PRO', 'Pro'),
    ('PRE', 'Premium')
)


# profile class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    age = models.IntegerField(default=18)
    phone = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    height = models.IntegerField(default=60)
    weight = models.IntegerField(default=100)
    membership = models.CharField(max_length=3, default=0, choices=PACKAGES)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
