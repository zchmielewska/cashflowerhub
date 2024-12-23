# Generated by Django 5.1.1 on 2024-11-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashflowmodel',
            old_name='short_description',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='cashflowmodel',
            name='repository_url',
            field=models.URLField(verbose_name='Repository URL'),
        ),
    ]
