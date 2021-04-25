from django.db import models
from django.urls import reverse


class Generator(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):  # строковый метод
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):  # строковый метод
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Prepod(models.Model):
    familiya_prepod = models.CharField(max_length=20)
    name_prepod = models.CharField(max_length=15)
    otchestvo = models.CharField(max_length=20)

    def __str__(self):  # строковый метод
        return self.familiya_prepod


class Discip(models.Model):
    discip_title = models.CharField(max_length=50)
    obyem_discip = models.IntegerField(default=0)
    zuv = models.ForeignKey('ZUV', on_delete=models.PROTECT, null=True,
                            verbose_name='Знать, уметь, владеть')

    def __str__(self):  # строковый метод
        return self.discip_title


class ZUV(models.Model):
    z = models.CharField(max_length=1000)
    u = models.CharField(max_length=1000)
    v = models.CharField(max_length=1000)
    compet = models.ForeignKey('Competence', on_delete=models.PROTECT, null=True,
                               verbose_name='Компетенция')


class Competence(models.Model):
    competence_text = models.CharField(max_length=50)
    description_competence = models.CharField(max_length=200)
    napr_pod = models.ForeignKey('NapravPodgotovki', on_delete=models.PROTECT, null=True,
                                 verbose_name='Направление подготовки')

    def __str__(self):  # строковый метод
        return self.competence_text


class NapravPodgotovki(models.Model):
    naprav_podgotovki_title = models.CharField(max_length=100)
    form_ed = models.ForeignKey('FormEducation', on_delete=models.PROTECT, null=True,
                                verbose_name='Форма образования')

    def __str__(self):  # строковый метод
        return self.naprav_podgotovki_title


class FormEducation(models.Model):
    form_education_title = models.CharField(max_length=10)
    god_nab = models.ForeignKey('GodNabora', on_delete=models.PROTECT, null=True, verbose_name='Год набора')

    def __str__(self):  # строковый метод
        return self.form_education_title


class GodNabora(models.Model):
    god_nabora_num = models.CharField(max_length=10)

    def __str__(self):  # строковый метод
        return self.god_nabora_num


class ParsBook(models.Model):
    description_b = models.TextField(blank=True, verbose_name='Библиографическая запись')
    ann_b = models.TextField(blank=True, verbose_name='Аннотация книги')

    def __str__(self):  # строковый метод
        return self.description_b

