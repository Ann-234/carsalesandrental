# Generated by Django 4.2 on 2023-05-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_carbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbooking',
            name='customer',
        ),
        migrations.AddField(
            model_name='carbooking',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='carbooking',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('Used', 'Used'), ('New', 'New')], max_length=50),
        ),
    ]
