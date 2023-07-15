# Generated by Django 4.2.1 on 2023-07-15 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_alter_year1_semester1_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='masscom_year4_semester2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('Final Year', 'Final Year')], max_length=20)),
                ('semester', models.CharField(choices=[('Second Semester', 'Second Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year4_semester1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('Final Year', 'Final Year')], max_length=20)),
                ('semester', models.CharField(choices=[('First Semester', 'First Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year3_semester2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('Third Year', 'Third Year')], max_length=20)),
                ('semester', models.CharField(choices=[('Second Semester', 'Second Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year3_semester1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('Third Year', 'Third Year')], max_length=20)),
                ('semester', models.CharField(choices=[('First Semester', 'First Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year2_semester2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('Second Year', 'Second Year')], max_length=20)),
                ('semester', models.CharField(choices=[('Second Semester', 'Second Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year2_semester1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('Second Year', 'Second Year')], max_length=20)),
                ('semester', models.CharField(choices=[('First Semester', 'First Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year1_semester2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('level', models.CharField(choices=[('First Year', 'First Year')], max_length=20)),
                ('semester', models.CharField(choices=[('Second Semester', 'Second Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='masscom_year1_semester1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('level', models.CharField(choices=[('First Year', 'First Year')], max_length=20)),
                ('semester', models.CharField(choices=[('First Semester', 'First Semester')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
    ]