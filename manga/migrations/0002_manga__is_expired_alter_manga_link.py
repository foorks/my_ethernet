# Generated by Django 4.0.3 on 2022-04-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='_is_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='manga',
            name='link',
            field=models.URLField(unique=True, verbose_name='Ссылка на аниме'),
        ),
    ]
