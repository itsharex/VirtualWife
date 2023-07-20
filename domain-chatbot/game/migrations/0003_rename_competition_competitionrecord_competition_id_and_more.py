# Generated by Django 4.2.1 on 2023-06-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_competition_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitionrecord',
            old_name='competition',
            new_name='competition_id',
        ),
        migrations.AlterField(
            model_name='competition',
            name='victor_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='胜利者名称'),
        ),
    ]
