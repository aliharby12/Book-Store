from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    override the base user manager to create a new user,
    create a superuser and add some additional features
    
    """
    def create_user(self, email : str, password:str) -> 'User':
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email : str, password : str) -> 'User':
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user