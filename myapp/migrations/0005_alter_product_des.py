# Generated by Django 3.2.6 on 2021-09-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.TextField(),
        ),
    ]
