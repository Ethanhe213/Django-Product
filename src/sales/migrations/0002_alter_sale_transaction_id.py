# Generated by Django 4.1.5 on 2023-01-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]