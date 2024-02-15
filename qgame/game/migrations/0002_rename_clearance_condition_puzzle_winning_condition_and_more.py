# Generated by Django 4.2.7 on 2023-11-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puzzle',
            old_name='clearance_condition',
            new_name='winning_condition',
        ),
        migrations.AddField(
            model_name='puzzle',
            name='cx_gate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='cz_gate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='level_number',
            field=models.IntegerField(default=1),
        ),
    ]
