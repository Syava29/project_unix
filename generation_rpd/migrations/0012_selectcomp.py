# Generated by Django 3.2 on 2021-05-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation_rpd', '0011_auto_20210506_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod_c', models.CharField(max_length=10)),
                ('descrip_c', models.TextField(blank=True, verbose_name='Формулировка компетенции')),
                ('kod_i_naim_c1', models.TextField(blank=True, verbose_name='Знать')),
                ('kod_i_naim_c2', models.TextField(blank=True, verbose_name='Уметь')),
                ('kod_i_naim_c3', models.TextField(blank=True, verbose_name='Владеть')),
            ],
        ),
    ]
