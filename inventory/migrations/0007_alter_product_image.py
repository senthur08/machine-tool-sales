# Generated by Django 5.1.2 on 2024-11-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to=''),
        ),
    ]
