# Generated by Django 2.2.6 on 2019-10-28 18:52

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20191028_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]