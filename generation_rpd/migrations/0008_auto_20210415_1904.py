# Generated by Django 3.1.7 on 2021-04-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation_rpd', '0007_parsbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsbook',
            name='ann_b',
            field=models.TextField(blank=True, verbose_name='Аннотация книги'),
        ),
        migrations.AlterField(
            model_name='parsbook',
            name='description_b',
            field=models.TextField(blank=True, verbose_name='Библиографическая запись'),
        ),
    ]