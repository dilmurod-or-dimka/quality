# Generated by Django 4.2 on 2023-05-09 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_services_options_alter_services_descr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.TextField(verbose_name='Описание описания сайта')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Описание сайта',
                'verbose_name_plural': 'Описании сайта',
            },
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Фото')),
                ('abouts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.about')),
            ],
        ),
    ]