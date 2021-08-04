from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='Bio...📰', max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

class UserManager(BaseUserManager):
    def create_user(self, name,email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not name:
            raise ValueError('Users must have a name')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, name,email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, name,email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            name,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=255, unique=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
        # The user is identified by their email address
		return self.email

	def get_short_name(self):
		return self.email


	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_active(self):
		return self.active

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin