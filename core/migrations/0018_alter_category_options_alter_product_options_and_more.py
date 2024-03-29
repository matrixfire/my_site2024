# Generated by Django 4.2.2 on 2024-02-27 14:31

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title'], 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='justaslug', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='justslug', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='product.jpg', upload_to=core.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='2.99', max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=10),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['title'], name='core_catego_title_4dd14c_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['pid', 'slug'], name='core_produc_pid_96278a_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['title'], name='core_produc_title_05e747_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-mfd'], name='core_produc_mfd_c4612a_idx'),
        ),
    ]
