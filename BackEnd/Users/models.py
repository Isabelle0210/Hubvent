from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, nome, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(nome=nome, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        return self.create_user(nome, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Necessário para acessar Django Admin

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_authenticated(self):
        return True  # Necessário para o Django reconhecer este usuário como autenticado

    @property
    def is_anonymous(self):
        return False  # Indica que não é um usuário anônimo
