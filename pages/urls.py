from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("services/", views.service_view, name="services"),
    path("blog/", views.blog_view, name="blog"),
    path("contact/", views.contact_view, name="contact"),
    path("blog/<slug:slug>/", views.blog_detail_view, name="blog_detail"),

    path("comments/<int:comment_id>/delete/", views.del_comment, name="del_comment"),

]