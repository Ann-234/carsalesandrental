# Generated by Django 4.2 on 2023-05-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0016_alter_carrental_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrental',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='carrental',
            name='start_date',
            field=models.DateField(),
        ),
    ]