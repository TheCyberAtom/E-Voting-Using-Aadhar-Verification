# Generated by Django 3.1.7 on 2021-03-28 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoting_app', '0011_auto_20210329_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 29, 3, 42, 24, 415311)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 29, 3, 42, 24, 415311)),
        ),
    ]