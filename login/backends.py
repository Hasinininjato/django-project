from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class EmailAuthBackend(BaseBackend):
	"""
		Email authentication backend.
		Allows a user to sign in using email/password pair rather rather than a username/password pair.
	"""

	def authenticate(self, username=None, password=None):
		"""
			Authenticate a user based on email as the user name
			:param username: email
			:param password: password
			:return:
		"""
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		"""
			Get a User object from the user_id
			:param user_id:
			:return:
		"""
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None