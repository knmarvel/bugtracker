# Generated by Django 3.0.6 on 2020-05-21 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='time_of_completion',
            new_name='completed_date',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='time_of_origin',
            new_name='reported_date',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='completed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('Deleted user'), related_name='completed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='reported_by',
            field=models.ForeignKey(on_delete=models.SET('Deleted user'), related_name='reported_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
