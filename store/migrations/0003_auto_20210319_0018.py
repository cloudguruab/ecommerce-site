# Generated by Django 3.1.7 on 2021-03-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210319_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='details',
            new_name='detailfour',
        ),
        migrations.AddField(
            model_name='product',
            name='detailone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='detailthree',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='detailtwo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
