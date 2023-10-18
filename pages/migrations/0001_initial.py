# Generated by Django 4.2 on 2023-04-29 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Имя человека')),
                ('descr', models.TextField(verbose_name='Описание человека')),
                ('does_work', models.BooleanField(default=True, verbose_name='Работает?')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название преимущества')),
                ('descr', models.TextField(verbose_name='Описание перимущества')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='ServicesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Фото')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.services')),
            ],
        ),
        migrations.CreateModel(
            name='HumanImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='humans/', verbose_name='Фото')),
                ('humans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.human')),
            ],
        ),
    ]
