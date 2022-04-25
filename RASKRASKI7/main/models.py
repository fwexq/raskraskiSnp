from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

class picture(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='image/', verbose_name='Фотография')

    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural ='Картинки'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


