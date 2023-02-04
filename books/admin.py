from django.contrib import admin
from .models import Author, Category, Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_date', 'is_active')  # listelenmek istenen fieldları göstermek icin
    list_filter = ('is_active', 'created_date', 'category')  # filtrelemek istediğimiz alanlar için kullanılır
    ordering = ('created_date',)  # sıralama icin kullanıkır
    search_fields = ('name', 'category', 'created_date', 'is_active')  # arama özelliğiæß
    list_per_page = 50  # sayfada kaç tane görünmesini istiyorsak
    actions = ('update_activate',)  # eklemek istediğimiz fonksiyon aksiyonlarını koyarız


    def update_activate(self, request, queryset):
        queryset.update(is_active=True)

    update_activate.short_description = "Seçili Nesneleri Yayına Al"  # actionun ismini düzenleme


admin.site.register(Author)
admin.site.register(Category)
