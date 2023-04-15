from django.contrib import admin
from .models import *


# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'published_date', 'list_authors')

#     def list_authors(self, obj):
#         return ", ".join([str(author) for author in obj.authors.all()])

@admin.register(Company)
class ComponyAdmin(admin.ModelAdmin):
    # df = Company.objects.all().values()
    # print(df)
    # def HozeieFaliat(self, obj):
        # return "، ".join([str(sabt) for sabt in obj.HozeieFaliat.all().values_list('HozeieFaliat__Childe')])
        # for sabt in obj.HozeieFaliat.all():
        #     print(type(sabt)) 
              
        # return "، ".join([str(sabt) for sabt in obj.HozeieFaliat.all()])

    list_display = ('FullName', 'Shenaseh', 
                    'ShenasehMeli', 'ShomarehSabt', 'KodeEghtesadi', 'CreateDate', 'Active', 'UserCreate', 'Order')


    # milad.short_description = 'شماره ثبت'

    list_filter = ['FullName']
    search_fields = ['FullName']
    ordering = ['FullName', 'Order']
    # date_hierarchy = ('CreateDate')
@admin.register(Preson)
class ComponyAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'CompanyRelation', 
                    'Departeman', 'CodeMeli', 'MahdodehieKari', 'Semat', 'sex', 'CreateDate', 'Active','UserCreate')
    list_filter = ['FullName']
    search_fields = ['FullName']
    ordering = ['FullName', 'Order']


admin.site.register(BaseHozeieAsliFaliatModel)
admin.site.register(BaseTaghismbandiKoli)
admin.site.register(BaseChaildeTaghismbandiKoli)
admin.site.register(Tozihat)
# admin.site.register(Company)
admin.site.register(BaseSemat)
# admin.site.register(Preson)
admin.site.register(BaseWebsiteTypeModel)
admin.site.register(BaseEmailTypeModel)
admin.site.register(BaseTellTypeModel)
admin.site.register(BaseAdressTypeModel)
admin.site.register(BaseSocialMediaTypeModel)
admin.site.register(BaseMessangerTypeModel)
admin.site.register(BaseStateModel)
admin.site.register(WbSiteCompony)
admin.site.register(EmailCompany)
admin.site.register(TellComony)
admin.site.register(AddressCompany)
admin.site.register(SocialNetworksCompany)
admin.site.register(MessangerCompany)
admin.site.register(WbSitePreson)
admin.site.register(EmailPreson)
admin.site.register(TellPreson)
admin.site.register(AddressPreson)
admin.site.register(SocialNetworksPreson)
admin.site.register(MessangerPreson)
