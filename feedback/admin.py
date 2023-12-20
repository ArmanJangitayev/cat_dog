from django.contrib import admin
from .models import Image, Cat, Dog, Feedback


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]


admin.site.register(Image, ImageAdmin)  # мы зарегистрируем нашу модель в admin.py


# Список list_display указывает администратору Django
# отображать его содержимое на панели администратора. Содержимое - это поля модели.

# В этом случае мы хотим, чтобы он отображдал
# поля заголовка и фотографии каждого загружаемого изображения.

class ImageCat(admin.ModelAdmin):
    list_display = ["name", "image"]


admin.site.register(Cat, ImageCat)


class ImageDog(admin.ModelAdmin):
    list_display = ["name", "image"]


admin.site.register(Dog, ImageDog)


class Feedback_Admin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "date_sent"]


admin.site.register(Feedback, Feedback_Admin)
