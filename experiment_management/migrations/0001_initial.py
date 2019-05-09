# Generated by Django 2.2 on 2019-05-09 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
                ('config_json', models.CharField(max_length=10000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperimentEnviroment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
                ('software_info', models.CharField(max_length=2000)),
                ('hardware_info', models.CharField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperimentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperimentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
                ('info', models.CharField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=2000)),
                ('source_file_path', models.CharField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExperimentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update date')),
                ('description', models.CharField(max_length=2000)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='experiment_management.Config')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='experiment_management.Experiment')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='experiment_management.Model')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='experiment',
            name='experiment_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='experiment_management.ExperimentGroup'),
        ),
        migrations.AddField(
            model_name='config',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='experiment_management.Experiment'),
        ),
    ]
