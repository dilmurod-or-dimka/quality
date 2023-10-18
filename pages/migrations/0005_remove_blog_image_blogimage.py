# Generated by Django 4.2 on 2023-05-12 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_blog_delete_aboutimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Фото')),
                ('humans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.blog')),
            ],
        ),
    ]