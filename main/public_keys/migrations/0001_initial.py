# Generated by Django 4.1.5 on 2023-02-06 05:42

from django.db import migrations, models
import django_extensions.validators
import public_keys.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('key', public_keys.models.HexadecimalField(max_length=512, validators=[django_extensions.validators.HexValidator(length=256)], verbose_name='public key')),
                ('prime_p', models.CharField(blank=True, max_length=256, null=True, verbose_name='prime number p')),
                ('curve_a', models.CharField(blank=True, max_length=256, null=True, verbose_name='curve a')),
                ('curve_b', models.CharField(blank=True, max_length=256, null=True, verbose_name='curve b')),
                ('order_q', models.CharField(blank=True, max_length=256, null=True, verbose_name='order q')),
                ('generator', models.CharField(blank=True, max_length=256, null=True, verbose_name='generator A')),
                ('cor_ver', models.CharField(blank=True, max_length=256, null=True, verbose_name='verification coordinate B')),
            ],
            options={
                'verbose_name': 'public key',
                'verbose_name_plural': 'public keys',
            },
        ),
    ]
