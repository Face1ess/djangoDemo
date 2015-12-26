# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_Act',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('T_ActDist', models.PositiveIntegerField(max_length=30)),
                ('T_ActDuration', models.CharField(max_length=60)),
                ('T_ActStartDate', models.CharField(max_length=30)),
                ('T_ActAvgSpd', models.DecimalField(max_digits=10, decimal_places=2)),
                ('T_ActCalBurn', models.PositiveIntegerField(max_length=30)),
            ],
        ),
    ]
