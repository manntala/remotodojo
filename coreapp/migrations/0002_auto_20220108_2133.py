# Generated by Django 3.2.9 on 2022-01-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv',
            name='owner',
        ),
        migrations.DeleteModel(
            name='OrderProcessModel',
        ),
        migrations.DeleteModel(
            name='OrderTemplate',
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Csv',
        ),
    ]