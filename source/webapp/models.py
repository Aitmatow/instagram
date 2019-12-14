from django.contrib.auth.models import User
from django.db import models




class Image(models.Model):
    image = models.ImageField(upload_to='', blank=False, null=False, verbose_name='Фотография')
    text = models.CharField(max_length=200, blank=False, null=False, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    likes = models.IntegerField(default=0, verbose_name='Количество лайков')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='image_user', verbose_name='Автор', null=True)
    users_like = models.ManyToManyField(User, related_name='image_liked', verbose_name='Лайк пользователя')


    def __str__(self):
        return self.text[:20] + '..'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural='Фотографии'

class Comment(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Текст', null=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comment_image', verbose_name='Фотография')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', verbose_name='Автор комментария')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return self.text[:20] + '..'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'