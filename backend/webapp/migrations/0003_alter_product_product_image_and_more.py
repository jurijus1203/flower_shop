# Generated by Django 4.2.16 on 2024-11-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_producttype_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('flowers', 'Flowers')], default='flowers', max_length=64),
        ),
    ]