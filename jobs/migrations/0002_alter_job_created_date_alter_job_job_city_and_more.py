# Generated by Django 4.0.3 on 2022-04-10 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_city',
            field=models.SmallIntegerField(choices=[(0, '北京'), (1, '上海'), (2, '深圳')], verbose_name='工作地点'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
    ]
