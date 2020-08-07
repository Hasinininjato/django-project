from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
	"""
		Custom user model manager by redefining create_user and create_superuser methods, and
		allows creating user with email/password pair.
	"""
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""
			Creates and saves a User with the given email and password.
			:param email: the user's email address | required
			:param password: the user's password
			:param extra_fields: extra fields about the user
			:return: user
		"""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""
			Creates and saves a simple user.
			:param email:
			:param password:
			:param extra_fields:
			:return: user
		"""
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""
			Creates and saves a super user
			:param email:
			:param password:
			:param extra_fields:
			:return: user
		"""
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)
