# Generated by Django 3.0.3 on 2021-12-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20211215_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='job',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='team',
            name='names',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='team',
            name='phrase',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Frase'),
        ),
    ]
