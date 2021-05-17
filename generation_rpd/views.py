from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
import sqlite3
from .models import Generator, Category, Prepod, Discip, GodNabora, FormEducation, NapravPodgotovki, ZUV, ParsBook, \
    Competence, ParsComp, SelectComp, TargetsAndTasks
from .forms import NewsForm, TestForm, PrepForm, UserRegisterForm, UserLoginForm, ContactForm, BasicDataForm, BasicForm, \
    BDForm, GandO, PlanResEd, CompSelect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
import requests
from bs4 import BeautifulSoup
from collections import Counter
from openpyxl import load_workbook
import re
from docx import Document


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'generation_rpd/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'generation_rpd/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(ListView):
    model = Generator
    template_name = 'generation_rpd/home_news_list.html'
    context_object_name = 'news'

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Generator.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = Generator
    template_name = 'generation_rpd/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Generator.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


# def index(request):
#     news = Generator.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'generation_rpd/index.html', context=context)


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'syava_test@mail.ru',
                             ['sevostyanov1999@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправленно!')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'generation_rpd/test.html', {"form": form})


def get_category(request, category_id):
    news = Generator.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    return render(request, 'generation_rpd/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    # news_item = Generator.objects.get(pk=news_id)
    news_item = get_object_or_404(Generator, pk=news_id)
    return render(request, 'generation_rpd/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = Generator.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'generation_rpd/add_news.html', {'form': form})


def add_prep(request):
    if request.method == 'POST':
        form = PrepForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = Generator.objects.create(**form.cleaned_data)
            prep = form.save()
            return redirect(prep)
    else:
        form = PrepForm()
    return render(request, 'generation_rpd/add_test.html', {'form': form})


def add_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            prep = Prepod.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = TestForm()
    return render(request, 'generation_rpd/add_test.html', {'form': form})


def add_basic_data(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            discip = form.save()
            return redirect('home')
    else:
        form = BasicForm()
    return render(request, 'generation_rpd/add_basic_data.html', {'form': form})


def add_test_data(request):
    if request.method == 'POST':
        form = BDForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            GodNabora.objects.create(god_nabora_num=form.cleaned_data['god_nabora_num'])
            NapravPodgotovki.objects.create(naprav_podgotovki_title=form.cleaned_data['naprav_podgotovki_title'])
            Discip.objects.create(discip_title=form.cleaned_data['discip_title'])
            FormEducation.objects.create(form_education_title=form.cleaned_data['form_education_title'])
            return redirect('generation_rpd/opn_main_window')
    else:
        form = BDForm()
    return render(request, 'generation_rpd/add_basic_data.html', {'form': form})


def add_goals(request):
    if request.method == 'POST':
        form = GandO(request.POST)
        if form.is_valid():
            TargetsAndTasks.objects.create(target=form.cleaned_data['g_a_o'], task=form.cleaned_data['task'],
                                           place_discip=form.cleaned_data['mesto_discip'])
            return redirect('add_plan_res_education')
    else:
        form = GandO()
    return render(request, 'generation_rpd/goals.html', {'form': form})


def opn_main_window(request):
    return render(request, 'generation_rpd/main_main.html')


def add_plan_res_ed(request):
    if request.method == 'POST':
        form = CompSelect(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = CompSelect()

    bd1 = SelectComp.objects.all()
    return render(request, 'generation_rpd/add_compet.html', {'form': form, 'bd1': bd1})


def connect_db(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM generation_rpd_prepod")
    one_result = cur.fetchmany(10)
    print(one_result)
    return render(request, 'generation_rpd/add_plan_res_ed.html')


def bd_test(request):
    bd = Prepod.objects.all()
    return render(request, "generation_rpd/home_news_list.html", {'bd': bd})


def parsing_book(request):
    lis = list(range(1000, 1083))
    list_book = []
    list_book_ann = []
    for i in lis:
        link = f'https://www.iprbookshop.ru/10{i}.html'
        website_url = requests.get(link).text
        soup = BeautifulSoup(website_url, 'lxml')

        items = soup.find_all('div', {'class': 'col-sm-12'})
        res = items[2].get_text()
        items1 = soup.find('meta', property="og:description")

        ParsBook.objects.create(description_b=''.join(res.split('\r\n\t')), ann_b=items1['content'])

    return render(request, "generation_rpd/home_news_list.html")


def get_comp(request):
    """ Название файлов """
    filename1 = "comp.xlsx"

    """ Списки """
    spisok_zuv = []
    spisok_komp = []
    description_zuv = []

    """ Считываем данные из excel """
    wb = load_workbook(filename1)
    sheet = wb['Лист1']

    """ Загружаем ЗУВы и разбиваем их на слова, а также удаляем Знать, Уметь, Владеть """
    for row in sheet['C1':'C35']:
        zuv = ''
        for cell in row:
            zuv = zuv + str(cell.value)
            your_string = zuv
            removal_list = ['Знать', 'Уметь', 'Владеть', ' и ', 'для', 'None', ' в ', ' на ', ' по ', 'знать', 'Задача',
                            'Лабораторная', 'Практикум', 'Краткое', 'cодержание', 'Задачи', 'Вариант', 'Основные',
                            ' с ', ' к ', ' при ']
            for word in removal_list:
                your_string = your_string.replace(word, '')
        description_zuv.append(your_string)
        result_key = re.findall(r'\w+', your_string)
        col_count = Counter(result_key).most_common(5)
        result_main23 = re.sub(r'\d', '', str(col_count))
        res_res = re.findall(r'\w+', result_main23)
        spisok_zuv.append(res_res)  # Список слов из ЗУВ для каждой компетенции для сравнния с литературой
        Competence.objects.create(description_competence=your_string)

    for row in sheet['A1':'A35']:
        string = ''
        for cell in row:
            string = string + str(cell.value)
            your_string = string

        spisok_komp.append(your_string)
        Competence.objects.create(competence_text=your_string)
    return render(request, "generation_rpd/home_news_list.html")


def get_commp(request):
    doc = Document('09_04_03.docx')
    # par = doc.paragraphs
    tbl = doc.tables
    n = []
    listt = []
    l = []
    i = 0
    while i < 2:
        for strok in tbl[0].rows:
            rr = strok.cells[i].text.strip()
            listt.append(''.join(rr.split('\n')))
            # Competence.objects.create(description_competence=''.join(rr.split('\n')))
        l.append(listt)
        i += 1

    for i in listt:
        if i not in n:
            n.append(i)
            Competence.objects.create(description_competence=i)

    bd = Competence.objects.all()

    return render(request, "generation_rpd/add_plan_res_ed.html", {'bd': bd})


def pars_test(table):
    listt1 = []
    listt2 = []
    listt3 = []
    l = []
    i = 0
    for strok in table[0].rows:
        rr = strok.cells[0].text.strip()
        listt1.append(''.join(rr.split('\n')))
    listt1.pop(0)
    l.append(listt1)
    for strok in table[0].rows:
        rr = strok.cells[1].text.strip()
        listt2.append(''.join(rr.split('\n')))
    listt2.pop(0)
    l.append(listt2)
    for strok in table[0].rows:
        rr = strok.cells[2].text.strip()
        listt3.append(''.join(rr.split('\n')))
    listt3.pop(0)
    l.append(listt3)
   # for iitems in listt:
          #      if iitems not in ll1:
             #       ll1.append(iitems)
    return(l)


def get_data_comp(request):
    doc = Document('09_04_03.docx')
    # par = doc.paragraphs
    i = 0

    tbl = doc.tables

    list_ret = []
    k = pars_test(tbl)
    l1 = list(k[0][0::3])
    list_ret.append(l1)
    l2 = list(k[1][0::3])
    list_ret.append(l2)
    l1_1 = list(k[2][1::3])
    list_ret.append(l1_1)
    l1_2 = list(k[2][2::3])
    list_ret.append(l1_2)
    l1_3 = list(k[2][0::3])
    list_ret.append(l1_3)

    #while i < len(l1):
     #   ParsComp.objects.create(kod_comp=l1[i], descrip_comp=l2[i], kod_i_naim_comp1=l1_3[i], kod_i_naim_comp2=l1_2[i],
      #                          kod_i_naim_comp3=l1_1[i])
       # i += 1

    bd = ParsComp.objects.all()
    return render(request, "generation_rpd/plan_res.html", {'bd': bd})


def add_plan_res_education(request):
    if request.method == 'POST':
        form = CompSelect(request.POST)
        listt = []
        list_1 = []
        list_2 = []
        list_3 = []
        k = ParsComp.objects.values_list('descrip_comp')
        k1 = ParsComp.objects.values_list('kod_i_naim_comp1')
        k2 = ParsComp.objects.values_list('kod_i_naim_comp2')
        k3 = ParsComp.objects.values_list('kod_i_naim_comp3')

        for items in k:
            listt.append(list(items))

        for items in k1:
            list_1.append(list(items))

        for items in k2:
            list_2.append(list(items))

        for items in k3:
            list_3.append(list(items))

        if form.is_valid():
            flag = 0
            k = str(form.cleaned_data['comp'])
            #print(list_1)
            for itt in listt:
                for i in itt:
                    if i == k:
                        print(list_1[flag][0], '+++')
                        print(list_2[flag][0], '+++')
                        print(list_3[flag][0], '+++')
                        SelectComp.objects.create(descrip_c=k, kod_i_naim_c1=list_1[flag][0], kod_i_naim_c2=list_3[flag][0],
                                                  kod_i_naim_c3=list_2[flag][0])

                        pass
                    flag += 1
            #if form.cleaned_data['comp'] ==
            return redirect('add_plan_res_education')
    else:
        form = CompSelect()

    bd1 = SelectComp.objects.all()
    print(bd1)
    return render(request, 'generation_rpd/add_compet.html', {'form': form, 'bd1': bd1})
