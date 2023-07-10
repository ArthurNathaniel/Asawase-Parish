# Generated by Django 4.1.7 on 2023-06-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0012_alter_payment_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('Welfare', 'Welfare'), ('Church', 'Church'), ('Harvest', 'Harvest')], max_length=20),
        ),
    ]