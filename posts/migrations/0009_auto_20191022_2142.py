# Generated by Django 2.2.4 on 2019-10-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20191022_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
