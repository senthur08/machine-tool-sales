# Generated by Django 5.1.2 on 2024-11-04 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
