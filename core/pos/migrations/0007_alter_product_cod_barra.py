# Generated by Django 3.2.2 on 2021-10-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_alter_product_cod_barra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cod_barra',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Código de Barra'),
        ),
    ]
