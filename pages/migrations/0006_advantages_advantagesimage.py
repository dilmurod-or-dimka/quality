# Generated by Django 4.2 on 2023-05-15 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_blog_image_blogimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название перимущества')),
                ('descr', models.TextField(verbose_name='Описание перимущества')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='advantages/', verbose_name='Фото')),
                ('advantages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.advantages')),
            ],
        ),
    ]
