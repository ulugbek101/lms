# Generated by Django 5.1.4 on 2025-01-02 02:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0003_alter_user_role_delete_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('lesson_days', models.CharField(choices=[('1-3-5', 'Du, Cho, Jum'), ('2-4-6', 'Se, Pay, Sha')], max_length=5)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('lesson_time', models.TimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_api.teacher')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('theme', models.CharField(max_length=200)),
                ('lesson_date', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_api.group')),
            ],
        ),
    ]