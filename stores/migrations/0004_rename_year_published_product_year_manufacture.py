# Generated by Django 4.2 on 2023-04-30 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='year_published',
            new_name='year_Manufacture',
        ),
    ]
