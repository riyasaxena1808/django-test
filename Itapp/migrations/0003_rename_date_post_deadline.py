# Generated by Django 4.0.6 on 2023-11-21 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Itapp', '0002_post_completed_alter_post_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='deadline',
        ),
    ]
