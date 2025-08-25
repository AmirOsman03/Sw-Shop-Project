from django.contrib import admin
from .models import Wishlist, WishlistProduct


# Inline за продукти во wishlist
class WishlistProductInline(admin.TabularInline):
    model = WishlistProduct
    extra = 0
    min_num = 0
    can_delete = True
    fields = ('product', 'size')
    readonly_fields = ()


# Главен Admin за Wishlist
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')
    inlines = [WishlistProductInline]
    ordering = ('user',)

    # Ограничи на superuser
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
