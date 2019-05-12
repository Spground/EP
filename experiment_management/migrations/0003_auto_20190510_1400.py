# Generated by Django 2.2 on 2019-05-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment_management', '0002_auto_20190510_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='experimentenvironment',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='experimentgroup',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='experimentlog',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='experimentrecord',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]