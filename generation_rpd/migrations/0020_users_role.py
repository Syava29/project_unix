# Generated by Django 3.2 on 2021-06-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generation_rpd', '0019_prepfio'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
