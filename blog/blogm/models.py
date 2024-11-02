from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Model, SET_NULL

User = get_user_model()

class BaseModel(models.Model):
    is_published = models.BooleanField(auto_created=True, verbose_name = 'Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Добавлено')
    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='Идентификатор')
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(BaseModel):
    name = models.CharField(max_length=256,verbose_name='Название места')
    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name

class Post(BaseModel):
    title = models.CharField(max_length=256, verbose_name = 'публикация')
    text = models.TextField(verbose_name = 'Текст')
    pub_date = models.DateTimeField(verbose_name = 'Дата и время публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
