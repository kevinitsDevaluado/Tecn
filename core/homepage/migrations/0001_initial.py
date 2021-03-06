# Generated by Django 3.0.3 on 2021-09-27 19:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('mobile', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('message', models.CharField(max_length=2000, verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-id'],
                'permissions': (('view_comments', 'Can view Comentarios'), ('delete_comments', 'Can delete Comentarios')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Título')),
                ('title', models.CharField(max_length=150, verbose_name='Subtítulo')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='departments/%Y/%m/%d', verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Departmento',
                'verbose_name_plural': 'Departmentos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='FreqQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Pregunta')),
                ('answer', models.TextField(verbose_name='Respuesta')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Preguntas Frecuente',
                'verbose_name_plural': 'Preguntas Frecuentes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/%Y/%m/%d', verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Galería',
                'verbose_name_plural': 'Galerias',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Mainpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ruc', models.CharField(max_length=13, verbose_name='Ruc')),
                ('proprietor', models.CharField(max_length=100, verbose_name='Propietario')),
                ('desc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Descripción')),
                ('with_us', models.CharField(blank=True, max_length=2000, null=True, verbose_name='¿Porque estar con nosotros?')),
                ('mission', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Misión')),
                ('vision', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Visión')),
                ('about_us', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Quienes Somos')),
                ('icon_image', models.ImageField(blank=True, null=True, upload_to='mainpage/%Y/%m/%d', verbose_name='Logo')),
                ('phone', models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='Teléfono Convencional')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Teléfono Celular')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='Correo Electrónico')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('horary', models.CharField(blank=True, max_length=50, null=True, verbose_name='Horario')),
                ('coordinates', models.CharField(blank=True, max_length=50, null=True, verbose_name='Coordenadas')),
                ('about_youtube', models.CharField(blank=True, max_length=250, null=True, verbose_name='Video de Youtube')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='IVA')),
            ],
            options={
                'verbose_name': 'Página Principal',
                'verbose_name_plural': 'Paginas Principales',
                'ordering': ['-id'],
                'permissions': (('view_mainpage', 'Can view Página Principal'),),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('desc', models.CharField(max_length=5000, verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d', verbose_name='Imagen')),
                ('url', models.TextField(verbose_name='Enlace web')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Qualities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Título')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='qualities/%Y/%m/%d', verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cualidad',
                'verbose_name_plural': 'Cualidades',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Título')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/%Y/%m/%d', verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css', models.CharField(max_length=50, verbose_name='Nombre de la clase css')),
                ('icon', models.CharField(max_length=100, verbose_name='Icono font-awesome')),
                ('url', models.CharField(max_length=150, verbose_name='Enlace')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/%Y/%m/%d', verbose_name='Imagen')),
                ('cant', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Estadística',
                'verbose_name_plural': 'Estadísticas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombre')),
                ('phrase', models.CharField(max_length=5000, verbose_name='Frase')),
                ('job', models.CharField(max_length=150, verbose_name='Profesión')),
                ('image', models.ImageField(blank=True, null=True, upload_to='team/%Y/%m/%d', verbose_name='Imagen')),
                ('desc', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Descripción')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Equipo de Trabajo',
                'verbose_name_plural': 'Equipos de Trabajo',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombre')),
                ('job', models.CharField(max_length=150, verbose_name='Profesión')),
                ('desc', models.CharField(max_length=5000, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/%Y/%m/%d', verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Testimonios',
                'verbose_name_plural': 'Testimonio',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('url', models.CharField(max_length=5000, verbose_name='Enlace')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TeamSocialNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('icon', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=500)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Team')),
            ],
            options={
                'verbose_name': 'Equipo de Trabajo | RedSocial',
                'verbose_name_plural': 'Equipos de Trabajo | RedSocial',
                'ordering': ['-id'],
                'default_permissions': (),
            },
        ),
    ]
