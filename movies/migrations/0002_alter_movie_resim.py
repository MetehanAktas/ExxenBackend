# Generated by Django 4.2.5 on 2023-10-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='resim',
            field=models.FileField(blank=True, null=True, upload_to='filmler', verbose_name='Film ismi giriniz'),
        ),
    ]
