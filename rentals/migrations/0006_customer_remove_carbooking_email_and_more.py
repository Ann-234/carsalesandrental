# Generated by Django 4.2 on 2023-05-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_remove_carbooking_customer_carbooking_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='carbooking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='carbooking',
            name='user_name',
        ),
        migrations.AddField(
            model_name='carbooking',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentals.customer'),
        ),
    ]
