# Generated by Django 5.0.1 on 2024-02-23 07:21

import cloudinary.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='full name')),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('PATIENT', 'Patient'), ('DOCTOR', 'Doctor'), ('NURSE', 'Nurse')], default='PATIENT', max_length=50, verbose_name='role')),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default='MALE', max_length=50, verbose_name='gender')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
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
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Department', models.CharField(choices=[('TAI MŨI HỌNG', 'Otorhinolaryngology'), ('PHỤ SẢN', 'Obstetrics Gynecology'), ('DA LIỄU', 'Dermatology'), ('THẨM MỸ', 'Plastic Surgery'), ('XƯƠNG KHỚP', 'Orthopedics'), ('MẮT', 'Ophthalmology'), ('RĂNG HÀM MẶT', 'Dentistry'), ('TÂM THẦN', 'Psychiatry'), ('Y HỌC CỔ TRUYỀN', 'Traditional Medicine'), ('NGOẠI TIẾT', 'Endocrinology')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('health_insurance', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('department', models.CharField(choices=[('TAI MŨI HỌNG', 'Otorhinolaryngology'), ('PHỤ SẢN', 'Obstetrics Gynecology'), ('DA LIỄU', 'Dermatology'), ('THẨM MỸ', 'Plastic Surgery'), ('XƯƠNG KHỚP', 'Orthopedics'), ('MẮT', 'Ophthalmology'), ('RĂNG HÀM MẶT', 'Dentistry'), ('TÂM THẦN', 'Psychiatry'), ('Y HỌC CỔ TRUYỀN', 'Traditional Medicine'), ('NGOẠI TIẾT', 'Endocrinology')], max_length=100)),
                ('booking_date', models.DateField(help_text='YY-MM-DD')),
                ('booking_time', models.TimeField()),
                ('status', models.CharField(choices=[('ĐÃ XÁC NHẬN', 'Confirmed'), ('CHƯA XÁC NHẬN', 'Unconfirmed'), ('ĐÃ HUỶ', 'Canceled'), ('ĐÃ THANH TOÁN', 'Paid'), ('CHƯA THANH TOÁN', 'Unpaid')], default='CHƯA XÁC NHẬN', max_length=100)),
                ('confirmed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nurse_confirm', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('patient', 'booking_date', 'booking_time')},
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
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('conclusion', models.CharField(blank=True, max_length=255)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='healthclinic.appointment', unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('appointment_fee', models.PositiveIntegerField()),
                ('prescription_fee', models.PositiveIntegerField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('TRỰC TIẾP', 'Direct'), ('MOMO', 'Momo'), ('ZALO_PAY', 'Zalo Pay')], max_length=100)),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='healthclinic.prescription', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrescriptionMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthclinic.medicine')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthclinic.prescription')),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='medicine_list',
            field=models.ManyToManyField(through='healthclinic.PrescriptionMedicine', to='healthclinic.medicine'),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='healthclinic.shift')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='healthclinic.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='shift',
            field=models.ManyToManyField(through='healthclinic.Schedule', to='healthclinic.shift'),
        ),
    ]
