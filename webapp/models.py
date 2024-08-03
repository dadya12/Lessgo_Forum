from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Topics(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(max_length=500, verbose_name='Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', verbose_name='Автор')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    answers_count = models.PositiveIntegerField(default=0, verbose_name='Количество ответов')

    def __str__(self):
        return self.name

