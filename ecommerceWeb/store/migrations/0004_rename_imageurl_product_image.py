# Generated by Django 4.1.1 on 2023-05-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_image_product_imageurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imageURL',
            new_name='image',
        ),
    ]
