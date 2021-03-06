# Generated by Django 3.1.7 on 2021-03-31 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generation_rpd', '0005_auto_20210330_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='competence',
            name='napr_pod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='generation_rpd.napravpodgotovki', verbose_name='Направление подготовки'),
        ),
        migrations.AddField(
            model_name='discip',
            name='zuv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='generation_rpd.zuv', verbose_name='Знать, уметь, владеть'),
        ),
        migrations.AddField(
            model_name='formeducation',
            name='god_nab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='generation_rpd.godnabora', verbose_name='Год набора'),
        ),
        migrations.AddField(
            model_name='napravpodgotovki',
            name='form_ed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='generation_rpd.formeducation', verbose_name='Форма образования'),
        ),
        migrations.AddField(
            model_name='zuv',
            name='compet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='generation_rpd.competence', verbose_name='Компетенция'),
        ),
    ]
