# Generated by Django 3.2.6 on 2021-09-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='des',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
