# Generated by Django 3.2 on 2021-05-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation_rpd', '0014_listcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.TextField(blank=True, verbose_name='Библиографическая запись')),
            ],
        ),
    ]