# Generated by Django 5.1.4 on 2025-01-02 01:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Superuser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
            bases=('app_api.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('superuser', 'Superadmin'), ('admin', 'Admin'), ('teacher', 'Ustoz'), ('parent', 'Ota-Ona'), ('student', "O'quvchi")], default='student', max_length=10),
        ),
    ]