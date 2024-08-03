# Generated by Django 5.0.7 on 2024-08-03 07:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_categorymodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'managed': True, 'verbose_name': 'Kategoriyalar', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='contactmodel',
            options={'managed': True, 'verbose_name': 'Aloqa', 'verbose_name_plural': 'Aloqalar'},
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='updeted_time',
            new_name='update_time',
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='body',
            field=models.TextField(verbose_name="Yangilik haqda ma'lumot"),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categorymodel', verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='create_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(upload_to='news/image', verbose_name='Rasim'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='publish_time',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Yangilik yaratish vaqti'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='status',
            field=models.CharField(choices=[('Deactive', 'Faol emasa'), ('Active', 'Faol')], default='Deactive', max_length=50, verbose_name='Holati'),
        ),
        migrations.AlterModelTable(
            name='categorymodel',
            table='Categories',
        ),
    ]
