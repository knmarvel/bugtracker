# Generated by Django 3.0.6 on 2020-05-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0002_auto_20200521_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Process', 'In Process'), ('Done', 'Done'), ('Invalid', 'Invalid')], max_length=10),
        ),
    ]
