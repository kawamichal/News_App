# Generated by Django 2.2.6 on 2019-10-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20191022_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
