# from django.utils import timezone
# from django.db import models


# class CategoryModel(models.Model):
#         name = models.CharField(max_length=50, verbose_name='Kategoriya nomi') 


#         class Meta:
#             db_table = 'Kategoriya'
#             managed = True
#             verbose_name = 'Kategoriya'
#             verbose_name_plural = 'Kategoriyalar'


# class ActivedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status='Active')


# class NewsModel(models.Model):

#     class Status(models.TextChoices):
#         Deactive = 'Faol emas', 'Faol emas'
#         Active = 'Faol', 'Faol'

#     title = models.CharField(max_length=250, verbose_name='Yangilik nomi')
#     body = models.TextField(verbose_name='Yangilik haqida malumotlar')
#     image = models.ImageField(upload_to='news/image', verbose_name='Rasmi')
#     category = models.ForeignKey(CategoryModel,
#                                  on_delete=models.CASCADE,
#                                  verbose_name='Kategoriyasiz'
#                                  )
#     publish_time = models.DateTimeField(default=timezone.now, verbose_name='Yangilik yaratilgan vaqt')
#     create_time = models.DateTimeField(auto_now_add=True)
#     updeted_time = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=50,
#                               choices=Status.choices,
#                               default=Status.Deactive,
#                               verbose_name='Holati'
#                               )
    
#     objects = models.Manager()
#     manager = ActivedManager()
    

#     class Meta:
#         ordering = ['-publish_time']
#         db_table = 'News'
#         managed = True
#         verbose_name = 'Yangiliklar'
#         verbose_name_plural = 'Yangiliklar'

#     def __str__(self):
#         return self.title


# class ContactModel(models.Model):

#     name = models.CharField(max_length=50,verbose_name='Ism')
#     email = models.EmailField(max_length=254, verbose_name='Email')
#     message = models.TextField(verbose_name='Xabar')

#     def __str__(self) -> str:
#         return self.email


#     class Meta:
#         db_table = 'Contact'
#         managed = True
#         verbose_name = 'Aloqa'
#         verbose_name_plural = 'Aloqa'


from django.utils import timezone
from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categories'  # 'Categorys' ni 'Categories' bilan almashtiring
        managed = True
        verbose_name = 'Kategoriyalar'
        verbose_name_plural = 'Kategoriyalar'


class ActivedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='Active')


class NewsModel(models.Model):
    class Status(models.TextChoices):
        DEACTIVE = 'Deactive', 'Faol emasa'
        ACTIVE = 'Active', 'Faol'

    title = models.CharField(max_length=250, verbose_name='Yangilik nomi')
    # slug = models.SlugField(max_length=250)
    body = models.TextField(verbose_name="Yangilik haqda ma'lumot")
    image = models.ImageField(upload_to='news/image', verbose_name='Rasim')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='Kategoriya')
    publish_time = models.DateField(default=timezone.now, verbose_name='Yangilik yaratish vaqti')
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)  # O'zgarishlarni qayd etish uchun DateTimeField
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.DEACTIVE,
        verbose_name='Holati'
    )

    objects = models.Manager()
    manager = ActivedManager()

    class Meta:
        ordering = ['-publish_time']
        db_table = 'News'
        managed = True
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ism')
    email = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Xabar')

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'Contact'
        managed = True
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'
