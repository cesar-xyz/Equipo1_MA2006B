# Generated by Django 4.1.5 on 2023-02-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('domain', models.CharField(max_length=512, verbose_name='domain url')),
            ],
            options={
                'verbose_name': 'control_center',
                'verbose_name_plural': 'control_centers',
            },
        ),
    ]
