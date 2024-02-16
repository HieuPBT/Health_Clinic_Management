# Generated by Django 5.0.1 on 2024-02-16 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthclinic', '0004_alter_appointment_confirmed_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('unit', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='healthclinic.medicinecategory')),
            ],
            options={
                'unique_together': {('name', 'category')},
            },
        ),
    ]
