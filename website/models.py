from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Добавьте дополнительные поля, если необходимо
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Или другое уникальное имя
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Или другое уникальное имя
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

# Create your models here.
class Roles(models.Model):
    tittle=models.CharField(max_length=50)
    code=models.IntegerField()

    def __str__(self) -> str:
        return self.tittle
class Predmet(models.Model):
    tittle=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tittle
class Mugalim(models.Model):
    fio=models.CharField(max_length=300)
    create_date=models.DateTimeField(default=timezone.now)
    avatar=models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение категории")
    login=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    phone=models.CharField(max_length=300)
    role_id=models.ForeignKey(Roles,on_delete=models.CASCADE)
    predmet_id=models.ForeignKey(Predmet,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.fio
class Class(models.Model):
    tittle=models.CharField(max_length=50)
    mugalim_id=models.ForeignKey(Mugalim,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.tittle

class Okuuchular(models.Model):
    fio=models.CharField(max_length=300)
    create_date=models.DateTimeField(default=timezone.now)
    avatar=models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение категории")
    login=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    phone=models.CharField(max_length=300)
    class_id=models.ForeignKey(Class,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.fio

class Raspisanie(models.Model):
    mugalim_id=models.ForeignKey(Mugalim,on_delete=models.CASCADE)
    klass_id=models.ForeignKey(Class,on_delete=models.CASCADE)
    date_start=models.DateTimeField(default=timezone.now)
    date_end=models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return "raspisanie"
class Posishenie(models.Model):
    create_date=models.DateTimeField(default=timezone.now)
    mugalim_id=models.ForeignKey(Mugalim,on_delete=models.CASCADE)
    okuuchu_id=models.ForeignKey(Okuuchular,on_delete=models.CASCADE)
    baa=models.IntegerField()
    active=models.BooleanField(default=True)
    predmet_id=models.ForeignKey(Predmet,on_delete=models.CASCADE,default=True)

    def __str__(self) -> str:
        return f"{str(self.baa)} {str(self.okuuchu_id)}"
class Janylyktar(models.Model):
    tittle=models.CharField(max_length=300)
    image=models.ImageField(upload_to='media/photo/%Y/%m/%d', verbose_name="изображение категории")
    message=models.CharField(max_length=400)
    mugalim_id=models.ForeignKey(Mugalim,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.tittle