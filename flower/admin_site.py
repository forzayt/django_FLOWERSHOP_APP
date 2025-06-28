from django.contrib.admin import AdminSite
from django.utils.html import format_html

class FlowerShopAdminSite(AdminSite):
    site_header = 'Flower Shop Administration'
    site_title = 'Flower Shop Admin Portal'
    index_title = 'Welcome to Flower Shop Administration'
    site_url = '/'
    
    def each_context(self, request):
        context = super().each_context(request)
        context['site_header'] = format_html(
            '<div style="display: flex; align-items: center;">'
            '<span style="font-size: 24px; color: #e91e63; margin-right: 10px;">🌸</span>'
            '<span style="font-size: 20px; font-weight: bold;">{}</span>'
            '</div>',
            self.site_header
        )
        return context

# Create custom admin site instance
flower_admin_site = FlowerShopAdminSite(name='flower_admin')

# Register models with custom admin site
from .models import login, user, staff, Products
from .admin import LoginAdmin, UserAdmin, StaffAdmin, ProductsAdmin

flower_admin_site.register(login, LoginAdmin)
flower_admin_site.register(user, UserAdmin)
flower_admin_site.register(staff, StaffAdmin)
flower_admin_site.register(Products, ProductsAdmin) 