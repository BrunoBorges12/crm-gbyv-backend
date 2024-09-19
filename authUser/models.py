from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user_default(self, email, password, first_name, last_name):
        if not email:
            raise ValueError("Por favor insira o email")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        db_table = "crm_users"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    objects: UserManager = UserManager()
    USERNAME_FIELD = (
        "email"  # faz que django entenda que ele é indentificador unico o email
    )


class UserAdmin(models.Model):
    class Meta:
        db_table = "crm_admin_data"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=30)


class UserClient(models.Model):
    class Meta:
        db_table = "crm_client_data"

    enterprise = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    tel = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    positon_enterprise = models.CharField(max_length=30, blank=True, null=True)
    andress = models.CharField(max_length=40)
    cep = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
