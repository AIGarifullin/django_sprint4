from django.contrib import admin

from .models import Category, Comment, Location, Post

# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        # 'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
admin.site.register(Comment)
