# Generated by Django 3.1.7 on 2021-05-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation_rpd', '0010_auto_20210506_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='parscomp',
            name='kod_i_naim_comp3',
            field=models.TextField(blank=True, verbose_name='Владеть'),
        ),
        migrations.AlterField(
            model_name='parscomp',
            name='kod_i_naim_comp2',
            field=models.TextField(blank=True, verbose_name='Уметь'),
        ),
    ]