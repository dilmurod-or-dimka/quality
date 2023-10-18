from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Services(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание услуги  ")
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_photo_service(self):
        photo = self.servicesimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://images.satu.kz/126101312_w640_h640_razdel-v-razrabotketovary.jpg"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"


class ServicesImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="services/", blank=True, null=True)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)


class Human(models.Model):
    title = models.CharField(verbose_name="Имя человека", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание человека")
    does_work = models.BooleanField(verbose_name="Работает?", default=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_photo_human(self):
        photo = self.humanimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://images.satu.kz/126101312_w640_h640_razdel-v-razrabotketovary.jpg"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


class HumanImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="humans/", blank=True, null=True)
    humans = models.ForeignKey(Human, on_delete=models.CASCADE)


class About(models.Model):
    descr = models.TextField(verbose_name="Описание описания сайта")
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.descr

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.descr)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Описание сайта"
        verbose_name_plural = "Описании сайта"


class Blog(models.Model):
    title = models.CharField(verbose_name="Название блога", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание блога")
    slug = models.SlugField(blank=True, null=True, unique=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.descr

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def get_photo_blog(self):
        photo = self.blogimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://images.satu.kz/126101312_w640_h640_razdel-v-razrabotketovary.jpg"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class BlogImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="blogs/", blank=True, null=True)
    humans = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name="Comment")
