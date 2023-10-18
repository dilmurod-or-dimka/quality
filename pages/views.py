from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, HttpResponse
from .models import Human, Services, About, Blog, Comment
from .forms import CommentForm, ContactForm
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
import requests


# Create your views here.

def home_view(request):
    humans = Human.objects.all()[:3]
    services = Services.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    context = {
        "services": services,
        "humans": humans,
        "blogs": blogs,
    }
    return render(request, "pages/index.html", context)


def about_view(request):
    humans = Human.objects.all()
    abouts = About.objects.all()
    services = Services.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    context = {
        "abouts": abouts,
        "humans": humans,
        "services": services,
        "blogs": blogs

    }
    return render(request, "pages/about.html", context)


def service_view(request):
    services = Services.objects.all()
    blogs = Blog.objects.all()[:3]
    context = {
        "services": services,
        "blogs": blogs
    }
    return render(request, "pages/services.html", context)


def blog_view(request):
    blogs = Blog.objects.all()

    services = Services.objects.all()[:3]
    paginator = Paginator(blogs, 4)
    page = request.GET.get("page")
    result = paginator.get_page(page)
    context = {
        "blogs": result,
        "services": services,
    }
    return render(request, "pages/blog.html", context)


def send_to_telegram(message):
    apiToken = '6340695368:AAEc_RX74Hb7zGpMB3gW_lLMT3ssw-v34N0'
    chatID = '-1001661400408'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }

            message = "\n".join(body.values())
            try:
                send_to_telegram(message)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect("home")
    else:
        form = ContactForm()

    services = Services.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    context = {
        "services": services,
        "blogs": blogs,
        "form": form,
    }
    return render(request, "pages/contact.html", context)


def blog_detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    services = Services.objects.all()[:3]
    comments = blog.comments.all()

    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.blog = blog
            form.save()
            return redirect("blog_detail", slug)

    else:
        form = CommentForm()

    context = {
        "blog": blog,
        "form": form,
        "comments": comments,
        "comments_count": comments.count(),
        "services": services,
    }
    return render(request, "pages/blog_detail.html", context)


def del_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.author or request.user.is_superuser:
        blog_id = comment.blog.slug
        comment.delete()
        return redirect("blog_detail", blog_id)
    else:
        raise PermissionDenied

# TODO:

# Сделано:
#  сделать что-то с контактом
#  создать детальную cтраницу для блока
#  создать регестрацию
#  создать модельки для блока
#  Сдлать укоротитель текста для блока
