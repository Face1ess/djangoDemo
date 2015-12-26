# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_act',
            name='T_ActCalBurn',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='t_act',
            name='T_ActDist',
            field=models.PositiveIntegerField(),
        ),
    ]
