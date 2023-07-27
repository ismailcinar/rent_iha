from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and save a normal user
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a superuser (admin)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)  # Mark the superuser as an admin

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)  # New field to identify admin users

    objects = CustomUserManager()

    class Meta:
        permissions = [
            ('can_add_uav', 'Can Add UAV'),
            ('can_change_uav', 'Can Change UAV'),
            ('can_delete_uav', 'Can Delete UAV'),
        ]

    def __str__(self):
        return self.username

@receiver(post_save, sender=CustomUser)
def create_user_permissions(sender, instance=None, created=False, **kwargs):
    if created and instance.is_admin:
        # Assign all permissions to superusers during user creation
        for permission in Permission.objects.all():
            instance.user_permissions.add(permission)


class UAV(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=100)
    rental_price = models.FloatField()  
    image = models.ImageField(upload_to='uav_images/',default='default_uav_image.jpg', blank=True) 

    def __str__(self):
        return f"{self.brand} {self.model}"


class RentalRecord(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    renting_member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser model for the relation

    def __str__(self):
        return f"{self.uav} - {self.renting_member}"
