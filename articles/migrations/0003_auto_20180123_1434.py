# Generated by Django 2.0.1 on 2018-01-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20180123_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(),
        ),
    ]
