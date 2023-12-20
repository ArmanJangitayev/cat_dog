from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')
    # В models.py мы создадим модель с двумя полями,
    # заголовком фотографии и фотографией
    # Upload_to говорит Джанго сохранить фотографию
    # в каталоге под названием pics в медиа-каталоге


class Cat(models.Model):
    name = models.CharField(max_length=10)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)


class Dog(models.Model):
    name = models.CharField(max_length=10)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
