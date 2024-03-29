# Generated by Django 4.1.5 on 2023-02-06 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('public_keys', '0001_initial'),
        ('auditors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('date', models.CharField(blank=True, max_length=64, verbose_name='date')),
                ('is_producing', models.BooleanField(blank=True, null=True, verbose_name='is producing?')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='quantity')),
                ('mac_emisor', models.CharField(blank=True, max_length=64, null=True, verbose_name='mac_emisor')),
                ('ip_receptor', models.CharField(blank=True, max_length=64, null=True, verbose_name='ip_receptor')),
                ('auditor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auditors', to='auditors.auditor', verbose_name='auditor')),
                ('public_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_keys', to='public_keys.publickey', verbose_name='public_key')),
            ],
            options={
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
            },
        ),
    ]
