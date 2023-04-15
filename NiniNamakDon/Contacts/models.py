from django.db import models
from django.conf import settings


class BaseHozeieAsliFaliatModel(models.Model):
    class Meta:
        verbose_name = 'جدول پایه نوع اصلی فعالیت'
        verbose_name_plural = 'جدول پایه نوع اصلی فعالیت'
    Name = models.CharField(max_length=30, verbose_name='سمت')

    def __str__(self):
        return self.Name


class BaseTaghismbandiKoli(models.Model):
    class Meta:
        verbose_name = 'جدول پایه حوزه فعالیت مادر'
        verbose_name_plural = 'جدول پایه حوزه فعالیت مادر'
    GroupName = models.CharField(
        max_length=20, verbose_name='گروه حوزه فعالیت مادر')

    def __str__(self):
        return self.GroupName


class BaseChaildeTaghismbandiKoli(models.Model):
    class Meta:
        verbose_name = 'جدول پایه حوزه فعالیت جزعی'
        verbose_name_plural = 'جدول پایه حوزه فعالیت جزعی'
    Father = models.ForeignKey(
        BaseTaghismbandiKoli, on_delete=models.CASCADE, verbose_name='تقسیم بندی کلی')
    Childe = models.CharField(max_length=20, verbose_name="تقسیم بندی جزعی")

    def __str__(self):
        return self.Childe


class Tozihat(models.Model):
    class Meta:
        verbose_name = 'جدول پایه توضیحات تکمیلی'
        verbose_name_plural = 'جدول پایه توضیحات تکمیلی'

    KindOgActivity = models.CharField(
        max_length=20, verbose_name="توضیحات تکمیلی")

    def __str__(self):
        return self.KindOgActivity


class Company(models.Model):

    FullName = models.CharField(max_length=100, verbose_name='نام کامل')
    HozeieAsliFaliat = models.ManyToManyField(
        BaseHozeieAsliFaliatModel, verbose_name='حوزه اصلی فعالیت')
    HozeieFaliat = models.ManyToManyField(
        BaseChaildeTaghismbandiKoli, verbose_name='حوزه فعالیت')
    TozihateKar = models.ManyToManyField(
        Tozihat, verbose_name='توضیحات تکمیلی')
    Shenaseh = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='شناسه')
    ShenasehMeli = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='شناسه ملی')
    ShomarehSabt = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='شماره ثبت')
    KodeEghtesadi = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='کد اقتصادی')
    CreateDate = models.TimeField(auto_now_add=True)
    Active = models.BooleanField(default=True, verbose_name='وضعیت مخاطب')
    UserCreate = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.PROTECT, verbose_name='کاربر ایجاد کننده')
    Order = models.IntegerField(default=10,
                                help_text='Lower number are going closer to the top in result set', verbose_name='ترتیب مرتب سازی')

    class Meta:
        # ordering = ['Order', '-CreateDate']
        verbose_name = 'کمپانی'
        verbose_name_plural = 'کمپانی'

    def __str__(self):
        return self.FullName


class BaseSemat(models.Model):
    class Meta:

        verbose_name = 'جدول پایه سمت شخص'
        verbose_name_plural = 'جدول پایه سمت شخص'
    Name = models.CharField(max_length=30, verbose_name='سمت')

    def __str__(self):
        return self.Name


class Preson(models.Model):

    Mel = 1
    Famel = 2
    Unknow = 3
    SexChoise = ((Mel, "مرد"), (Famel, "زن"), (Unknow, "نامشخص"))
    FullName = models.CharField(max_length=100, verbose_name='')

    HozeieAsliFaliat = models.ManyToManyField(
        BaseHozeieAsliFaliatModel, verbose_name='حوزه اصلی فعالیت')
    HozeieFaliat = models.ManyToManyField(
        BaseChaildeTaghismbandiKoli, verbose_name='حوزه فعالیت')
    TozihateKar = models.ManyToManyField(
        Tozihat, verbose_name='توضیحات تکمیلی')
    CompanyRelation = models.ForeignKey(
        'Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='مرتبط با کمپانی')

    Departeman = models.CharField(
        max_length=21, null=True, blank=True, verbose_name='دپارتمان')
    CodeMeli = models.CharField(
        max_length=14, null=True, blank=True, verbose_name='کد ملی')
    MahdodehieKari = models.CharField(
        max_length=21, null=True, blank=True, verbose_name='محدوده کاری')
    Semat = models.ForeignKey(
        'BaseSemat', on_delete=models.CASCADE, verbose_name='سمت کاری')
    sex = models.IntegerField(
        choices=SexChoise, default=3, verbose_name='جنسیت')
    CreateDate = models.TimeField(auto_now_add=True)
    Active = models.BooleanField(default=True, verbose_name='وضعیت')
    UserCreate = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.PROTECT)
    Order = models.IntegerField(blank=False, null=True, default=0,
                                help_text='Lower number are going closer to the top in result set', verbose_name='ردیف مرتب سازی')

    class Meta:
        # ordering = ['Order', '-CreateDate']
        verbose_name = 'شخص'
        verbose_name_plural = 'شخص'

    def __str__(self):
        return self.FullName


class BaseWebsiteTypeModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نوع وب سایت'
        verbose_name_plural = 'جدول پایه نوع وب سایت'
    WebsiteType = models.CharField(max_length=30, verbose_name='نوع وبسایت')

    def __str__(self):
        return self.WebsiteType


class BaseEmailTypeModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نوع ایمیل'
        verbose_name_plural = 'جدول پایه نوع ایمیل'
    EmailTypeModel = models.CharField(max_length=30, verbose_name='نوع ایمیل')

    def __str__(self):
        return self.EmailTypeModel


class BaseTellTypeModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نوع تلفن'
        verbose_name_plural = 'جدول پایه نوع تلفن'
    TellType = models.CharField(max_length=30, verbose_name='نوع تلفن')

    def __str__(self):
        return self.TellType


class BaseAdressTypeModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نوع آدرس'
        verbose_name_plural = 'جدول پایه نوع آدرس'
    AdressType = models.CharField(max_length=30, verbose_name='نوع آدرس')

    def __str__(self):
        return self.AdressType


class BaseSocialMediaTypeModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نام مولتی مدیا'
        verbose_name_plural = 'جدول پایه نام مولتی مدیا'
    SocialMedia = models.CharField(
        max_length=30, verbose_name='نام مولتی مدیا')

    def __str__(self):
        return self.SocialMedia


class BaseMessangerTypeModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نام مسنجر ها'
        verbose_name_plural = 'جدول پایه نام مسنجر ها'
    SocialMedia = models.CharField(
        max_length=30, verbose_name='نوع پیامرسان')

    def __str__(self):
        return self.SocialMedia


class BaseStateModel(models.Model):
    class Meta:

        verbose_name = 'جدول پایه نام استان'
        verbose_name_plural = 'جدول پایه نام استان'
    State = models.CharField(max_length=30, verbose_name='نام استان')

    def __str__(self):
        return self.State


class WbSiteCompony(models.Model):
    class Meta:

        verbose_name = 'وب سایت کمپانی'
        verbose_name_plural = 'وب سایت کمپانی'
    Name = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='مرتبط با کمپانی')
    Group = models.ForeignKey(BaseWebsiteTypeModel,
                              on_delete=models.CASCADE, verbose_name='نوع وبسایت')
    TellNumber = models.CharField(max_length=200, verbose_name='آدرس سایت')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.TellNumber}"


class EmailCompany(models.Model):
    class Meta:

        verbose_name = 'ایمیل کمپانی'
        verbose_name_plural = 'ایمیل کمپانی'
    Name = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='مرتبط با کمپانی')
    Group = models.ForeignKey(
        BaseEmailTypeModel, on_delete=models.CASCADE, verbose_name='نوع ایمیل')
    TellNumber = models.EmailField(verbose_name='ایمیل')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.TellNumber}"


class TellComony(models.Model):
    class Meta:

        verbose_name = 'تلفن کمپانی'
        verbose_name_plural = 'تلفن کمپانی'
    Name = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='مرتبط با کمپانی')
    Group = models.ForeignKey(
        BaseTellTypeModel, on_delete=models.CASCADE, verbose_name='نوع تلفن')
    TellNumber = models.CharField(max_length=100, verbose_name='تلفن')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.TellNumber}"


class AddressCompany(models.Model):
    class Meta:

        verbose_name = 'آدرس کمپانی'
        verbose_name_plural = 'آدرس کمپانی'
    contacts = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name='مرتبط با کمپانی')
    type = models.ForeignKey("BaseAdressTypeModel",
                             on_delete=models.PROTECT, null=True, blank=True, verbose_name='نوع آدرس')
    street = models.CharField(max_length=50, null=True,
                              blank=True, verbose_name='خیابان')
    city = models.CharField(max_length=40, null=True,
                            blank=True, verbose_name='شهر')
    State = models.ForeignKey(
        "BaseStateModel", on_delete=models.CASCADE, null=True, blank=True, verbose_name='استان')
    zip = models.CharField(max_length=10, null=True,
                           blank=True, verbose_name='کد پستی')
    OtherText = models.TextField(
        null=True, blank=True, verbose_name='ادامه آدرس')

    def __str__(self):
        return self.contacts


class SocialNetworksCompany(models.Model):
    class Meta:

        verbose_name = 'مولتی مدیا کمپانی'
        verbose_name_plural = 'مولتی مدیا کمپانی'
    Name = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='مرتبط با کمپانی')
    Group = models.ForeignKey(BaseSocialMediaTypeModel,
                              on_delete=models.CASCADE, verbose_name='نوع سوشیال مدیا')
    IDNumbers = models.CharField(max_length=100, verbose_name='لینک')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.IDNumbers}"


class MessangerCompany(models.Model):
    class Meta:

        verbose_name = 'پیغامگیر های کمپانی'
        verbose_name_plural = 'پیغامگیر های کمپانی'
    Name = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='مرتبط با کمپانی')
    Group = models.ForeignKey(BaseMessangerTypeModel,
                              on_delete=models.CASCADE, verbose_name='پیام رسان')
    Numbers = models.CharField(max_length=100, verbose_name='شماره')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.Numbers}"


class WbSitePreson(models.Model):
    class Meta:

        verbose_name = 'سایت شخص'
        verbose_name_plural = 'سایت شخص'
    Name = models.ForeignKey(
        Preson, on_delete=models.CASCADE, verbose_name='مرتبط با شخص')
    Group = models.ForeignKey(BaseWebsiteTypeModel,
                              on_delete=models.CASCADE, verbose_name='نوع وبسایت')
    TellNumber = models.CharField(max_length=20, verbose_name='آدرس وبسایت')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.TellNumber}"


class EmailPreson(models.Model):
    class Meta:

        verbose_name = 'ایمیل شخص'
        verbose_name_plural = 'ایمیل شخص'
    Name = models.ForeignKey(
        Preson, on_delete=models.CASCADE, verbose_name='مرتبط با شخص')
    Group = models.ForeignKey(
        BaseEmailTypeModel, on_delete=models.CASCADE, verbose_name='نوع ایمیل')
    TellNumber = models.EmailField(verbose_name='ایمیل')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.TellNumber}"


class TellPreson(models.Model):
    class Meta:

        verbose_name = 'تلفن تماس شخص'
        verbose_name_plural = 'تلفن تماس شخص'
    Name = models.ForeignKey(
        Preson, on_delete=models.CASCADE, verbose_name='مرتبط با شخص')
    Group = models.ForeignKey(
        BaseTellTypeModel, on_delete=models.CASCADE, verbose_name='نوع تلفن')
    TellNumber = models.CharField(max_length=100, verbose_name='شماره')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.TellNumber}"


class AddressPreson(models.Model):
    class Meta:

        verbose_name = 'آدرس شخص'
        verbose_name_plural = 'آدرس شخص'
    contacts = models.ForeignKey(
        Preson, on_delete=models.PROTECT, verbose_name='مرتبط با شخص')
    type = models.ForeignKey("BaseAdressTypeModel",
                             on_delete=models.PROTECT, null=True, blank=True, verbose_name='نوع آدرس')

    street = models.CharField(max_length=50, null=True,
                              blank=True, verbose_name='خیابان')
    city = models.CharField(max_length=40, null=True,
                            blank=True, verbose_name='شهر')
    State = models.ForeignKey("BaseStateModel",
                              on_delete=models.CASCADE, null=True, blank=True, verbose_name='استان')
    zip = models.CharField(max_length=10, null=True,
                           blank=True, verbose_name='کد پستی')
    OtherText = models.TextField(
        null=True, blank=True, verbose_name='ادامه آدرس')

    def __str__(self):
        return self.contacts


class SocialNetworksPreson(models.Model):
    class Meta:

        verbose_name = 'مولتی مدیا شخص'
        verbose_name_plural = 'مولتی مدیا شخص'
    Name = models.ForeignKey(
        Preson, on_delete=models.CASCADE, verbose_name='مرتبط با شخص')
    Group = models.ForeignKey(BaseSocialMediaTypeModel,
                              on_delete=models.CASCADE, verbose_name='نوع مولتی مدیا')
    IDNumber = models.CharField(max_length=100, verbose_name='آیدی')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.IDNumber}"


class MessangerPreson(models.Model):
    class Meta:

        verbose_name = 'پیغامگیر شخص'
        verbose_name_plural = 'پیغامگیر شخص'
    Name = models.ForeignKey(
        Preson, on_delete=models.CASCADE, verbose_name='مرتبط با شخص')
    Group = models.ForeignKey(BaseMessangerTypeModel,
                              on_delete=models.CASCADE, verbose_name='نوع مسنجر')
    Numbers = models.CharField(max_length=100, verbose_name='شماره')

    def __str__(self):
        return f"{self.Name}  {self.Group}: {self.Numbers}"
