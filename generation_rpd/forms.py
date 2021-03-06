from django import forms
from .models import Generator, Prepod, Discip, GodNabora, FormEducation, NapravPodgotovki, Competence, ParsComp, \
    ParsBook, PrepFIO, RecomendBoook, Strings
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя в системе', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    otchestvo = forms.CharField(label='Отчество', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    role_prep = forms.ModelChoiceField(empty_label=None, queryset=Strings.objects.all(),
                                  label='Роль(Преподователь или Руководитель?)',
                                  widget=forms.Select(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвержение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', help_text='Пример: test@gmail.com', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'otchestvo', 'email', 'password1', 'password2', 'role_prep', 'username')


class NewsForm(forms.ModelForm):
    class Meta:
        model = Generator
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class PrepForm(forms.ModelForm):
    class Meta:
        model = Prepod
        fields = ['familiya_prepod', 'name_prepod', 'otchestvo']
        widgets = {
            'familiya_prepod': forms.TextInput(attrs={"class": "form-control"}),
            'name_prepod': forms.TextInput(attrs={"class": "form-control"}),
            'otchestvo': forms.TextInput(attrs={"class": "form-control"})
        }


class TestForm(forms.Form):
    familiya_prepod = forms.CharField(max_length=50, label='Фамилия',
                                      widget=forms.TextInput(attrs={"class": "form-control"}))
    name_prepod = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(attrs={"class": "form-control"}))
    otchestvo = forms.CharField(max_length=50, label='Отчество',
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    # discip = forms.ModelChoiceField(empty_label=None, queryset=Discip.objects.all(), label='Закреплённая дисциплина',
    # widget=forms.Select(attrs={"class": "form-control"}))


class BasicDataForm(forms.Form):
    god_nabora_num = forms.CharField(max_length=50, label='Год набора',
                                     widget=forms.TextInput(attrs={"class": "form-control"}))
    naprav_podgotovki_title = forms.CharField(max_length=50, label='Направ',
                                              widget=forms.TextInput(attrs={"class": "form-control"}))
    discip_title = forms.CharField(max_length=50, label='Дисцип',
                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    form_education_title = forms.CharField(max_length=50, label='Форма',
                                           widget=forms.TextInput(attrs={"class": "form-control"}))


class BasicForm(forms.ModelForm):
    class Meta:
        model = GodNabora
        # fields = '__all__'
        fields = ['god_nabora_num']
        widgets = {
            'god_nabora_num': forms.TextInput(attrs={'class': 'form-control'})
        }


class BDForm(forms.Form):
    # god_nabora_num = forms.CharField(label='Год набора', widget=forms.TextInput(attrs={"class": "form-control"}))
    # naprav_podgotovki_title = forms.CharField(label='Направ', widget=forms.TextInput(attrs={"class": "form-control"}))
    # discip_title = forms.CharField(label='Дисцип', widget=forms.TextInput(attrs={"class": "form-control"}))
    # obyem_discip = forms.IntegerField(label='Объём', widget=forms.TextInput(attrs={"class": "form-control"}))
    # form_education_title = forms.CharField(label='Форма', widget=forms.TextInput(attrs={"class": "form-control"}))
    god_nabora_num = forms.ModelChoiceField(empty_label=None, queryset=GodNabora.objects.all(), label='Год набора',
                                            widget=forms.Select(attrs={"class": "form-control"}))
    naprav_podgotovki_title = forms.ModelChoiceField(empty_label=None, queryset=NapravPodgotovki.objects.all(),
                                                     label='Направ',
                                                     widget=forms.Select(attrs={"class": "form-control"}))
    discip_title = forms.ModelChoiceField(empty_label=None, queryset=Discip.objects.all(), label='Дисцип',
                                          widget=forms.Select(attrs={"class": "form-control"}))
    # obyem_discip = forms.ModelChoiceField(empty_label=None, queryset=Discip.objects.all(), label='Объём',
    # widget=forms.Select(attrs={"class": "form-control"}))
    form_education_title = forms.ModelChoiceField(empty_label=None, queryset=FormEducation.objects.all(), label='Форма',
                                                  widget=forms.Select(attrs={"class": "form-control"}))


class GandO(forms.Form):
    g_a_o = forms.CharField(label='Цели', widget=forms.Textarea(attrs={"class": "form-control"}))
    task = forms.CharField(label='Задачи', widget=forms.Textarea(attrs={"class": "form-control"}))
    mesto_discip = forms.CharField(label='Место дисциплины', widget=forms.Textarea(attrs={"class": "form-control"}))


class PlanResEd(forms.Form):
    comp = forms.ModelChoiceField(empty_label=None, queryset=Competence.objects.all(), label='Компетенция',
                                  widget=forms.Select(attrs={"class": "form-control"}))
    g_a = forms.CharField(label='Описание компетенции', widget=forms.Textarea(attrs={"class": "form-control"}))
    z = forms.CharField(label='Знать', widget=forms.TextInput(attrs={"class": "form-control"}))
    u = forms.CharField(label='Уметь', widget=forms.TextInput(attrs={"class": "form-control"}))
    v = forms.CharField(label='Владеть', widget=forms.TextInput(attrs={"class": "form-control"}))


class StructDiscip(forms.Form):
    timee = forms.ModelChoiceField(empty_label=None, queryset=ParsComp.objects.all(), label='Часы',
                                   widget=forms.Select(attrs={"class": "form-control"}))
    classes = forms.ModelChoiceField(empty_label=None, queryset=ParsComp.objects.all(), label='Занятия',
                                     widget=forms.Select(attrs={"class": "form-control"}))
    form_ex = forms.ModelChoiceField(empty_label=None, queryset=ParsComp.objects.all(), label='Форма аттестации',
                                     widget=forms.Select(attrs={"class": "form-control"}))


class CompSelect(forms.Form):
    comp = forms.ModelChoiceField(empty_label=None, queryset=ParsComp.objects.all(), label='Компетенция',
                                  widget=forms.Select(attrs={"class": "form-control"}))


class Books(forms.Form):
    an_book = forms.CharField(label='Добавьте библиографическую запись',
                              widget=forms.Textarea(attrs={"class": "form-control"}))
    offer_books = forms.ModelChoiceField(empty_label=None, queryset=RecomendBoook.objects.all(),
                                         label='Предложение литературы',
                                         widget=forms.Select(attrs={"class": "form-control"}))


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class ROPHead(forms.Form):
    prep = forms.ModelChoiceField(empty_label=None, queryset=PrepFIO.objects.all(),
                                         label='ФИО преподавателя',
                                         widget=forms.Select(attrs={"class": "form-control"}))
    discip = forms.ModelChoiceField(empty_label=None, queryset=Discip.objects.all(),
                                         label='Дисциплина',
                                         widget=forms.Select(attrs={"class": "form-control"}))


class AddPrep(forms.Form):
    fio = forms.CharField(label='ФИО преподавателя',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
