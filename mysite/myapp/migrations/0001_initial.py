# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'null', max_length=100)),
                ('password', models.CharField(default=b'null', max_length=100)),
                ('name', models.CharField(default=b'null', max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('department_id', models.CharField(default=b'null', max_length=11)),
                ('desc', models.CharField(default=b'null', max_length=255)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('last_login_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
