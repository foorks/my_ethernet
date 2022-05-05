# Generated by Django 4.0.3 on 2022-04-02 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weathers', '0002_alter_weather_today_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_today',
            name='datetime',
            field=models.CharField(max_length=20, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='weather_today',
            name='sunrise',
            field=models.CharField(max_length=20, verbose_name='Восход'),
        ),
        migrations.AlterField(
            model_name='weather_today',
            name='sunset',
            field=models.CharField(max_length=20, verbose_name='Закат'),
        ),
    ]
