from django.contrib import admin
from .models import Post, LuckyDay, NotePost

# Register your models here.
admin.site.register(Post)
admin.site.register(LuckyDay)
admin.site.register(NotePost)