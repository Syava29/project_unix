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


class ListContent(models.Model):
    content = models.CharField(max_length=150)

    def __str__(self):  # строковый метод
        return self.content


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


class ParsComp(models.Model):
    kod_comp = models.CharField(max_length=10)
    descrip_comp = models.TextField(blank=True, verbose_name='Формулировка компетенции')
    kod_i_naim_comp1 = models.TextField(blank=True,
                                        verbose_name='Знать')
    kod_i_naim_comp2 = models.TextField(blank=True,
                                        verbose_name='Уметь')
    kod_i_naim_comp3 = models.TextField(blank=True,
                                        verbose_name='Владеть')

    def __str__(self):  # строковый метод
        return self.descrip_comp


class SelectComp(models.Model):
    kod_c = models.CharField(max_length=10)
    descrip_c = models.TextField(blank=True, verbose_name='Формулировка компетенции')
    kod_i_naim_c1 = models.TextField(blank=True,
                                     verbose_name='Знать')
    kod_i_naim_c2 = models.TextField(blank=True,
                                     verbose_name='Уметь')
    kod_i_naim_c3 = models.TextField(blank=True,
                                     verbose_name='Владеть')

    def __str__(self):  # строковый метод
        return self.descrip_c


class SelectBooks(models.Model):
    book = models.TextField(blank=True, verbose_name='Библиографическая запись')

    def __str__(self):  # строковый метод
        return self.book


class TargetsAndTasks(models.Model):
    target = models.TextField(blank=True, verbose_name='Цели и задачи')
    task = models.TextField(blank=True, verbose_name='Знать')
    place_discip = models.TextField(blank=True, verbose_name='Знать')

    def __str__(self):  # строковый метод
        return self.target


class RecomendBoook(models.Model):
    desc = models.TextField(blank=True, verbose_name='Библиографическая запись')

    def __str__(self):  # строковый метод
        return self.desc
