from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernotModelAdmin


@admin.register(Post)
class PostAdmin(SummernotModelAdmin):

    summernote_fields = ('content')


