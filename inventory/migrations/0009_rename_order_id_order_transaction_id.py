# Generated by Django 5.1.2 on 2024-11-05 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='transaction_id',
        ),
    ]
