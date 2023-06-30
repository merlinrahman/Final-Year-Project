# Generated by Django 4.2.1 on 2023-06-29 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExamsYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicyear', models.CharField(choices=[('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.department')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(choices=[('Bachelor of Science (BSc)', 'Bachelor of Science (BSc)'), ('Bachelor of Arts (BA)', 'Bachelor of Arts (BA)'), ('Bachelor of Business Administration (BBA)', 'Bachelor of Business Administration (BBA)'), ('Bachelor of Engineering (BEng)', 'Bachelor of Engineering (BEng)'), ('Bachelor of Education (BEd)', 'Bachelor of Education (BEd)'), ('Master of Science (MSc)', 'Master of Science (MSc)'), ('Master of Arts (MA)', 'Master of Arts (MA)'), ('Master of Business Administration (MBA)', 'Master of Business Administration (MBA)'), ('Master of Engineering (MEng)', 'Master of Engineering (MEng)'), ('Master of Education (MEd)', 'Master of Education (MEd)'), ('Diploma in Computer Science', 'Diploma in Computer Science'), ('Diploma in Graphics Design', 'Diploma in Graphics Design'), ('Diploma in Accounting', 'Diploma in Accounting'), ('Diploma in Banking and Finance', 'Diploma in Banking and Finance'), ('HND in Journalism', 'HND in Journalism'), ('HND in Business Administration', 'HND in Business Administration'), ('HND in Radio Broadcasting', 'HND in Radio Broadcasting'), ('HND in Radio English Language', 'HND in Radio English Language'), ('Certificate in Computer Studies', 'Certificate in Computer Studies'), ('Certificate in Project Management', 'Certificate in Project Management'), ('Certificate in Web Development ', 'Certificate in Web Development ')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.TextField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('level', models.TextField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Final Year', 'Final Year')], max_length=50)),
                ('dob', models.DateField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.department')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.program')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('academicYear', models.TextField(choices=[('2000/2001', '2000/2001'), ('2001/2002', '2001/2002'), ('2002/2003', '2002/2003'), ('2003/2004', '2003/2004'), ('2004/2005', '2004/2005'), ('2005/2006', '2005/2006'), ('2006/2007', '2006/2007'), ('2007/2008', '2007/2008'), ('2008/2009', '2008/2009'), ('2009/2010', '2009/2010'), ('2010/2011', '2010/2011'), ('2011/2012', '2011/2012'), ('2012/2013', '2012/2013'), ('2013/2014', '2013/2014'), ('2014/2015', '2014/2015'), ('2015/2016', '2015/2016'), ('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023')], max_length=20)),
                ('level', models.TextField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Final Year', 'Final Year')], max_length=50)),
                ('semester', models.TextField(choices=[('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')], max_length=50)),
                ('module_grade1', models.IntegerField()),
                ('module_grade2', models.IntegerField()),
                ('module_grade3', models.IntegerField()),
                ('module_grade4', models.IntegerField()),
                ('module_grade5', models.IntegerField()),
                ('module_grade6', models.IntegerField()),
                ('gradepoint1', models.TextField(max_length=2)),
                ('gradepoint2', models.TextField(max_length=2)),
                ('gradepoint3', models.TextField(max_length=2)),
                ('gradepoint4', models.TextField(max_length=2)),
                ('gradepoint5', models.TextField(max_length=2)),
                ('gradepoint6', models.TextField(max_length=2)),
                ('total_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sgp', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sch', models.IntegerField(default=3, null=True)),
                ('totalsch', models.IntegerField(default=0, null=True)),
                ('equivalent1', models.IntegerField(default=0, null=True)),
                ('equivalent2', models.IntegerField(default=0, null=True)),
                ('equivalent3', models.IntegerField(default=0, null=True)),
                ('equivalent4', models.IntegerField(default=0, null=True)),
                ('equivalent5', models.IntegerField(default=0, null=True)),
                ('equivalent6', models.IntegerField(default=0, null=True)),
                ('grade1', models.CharField(blank=True, max_length=1, null=True)),
                ('grade2', models.CharField(blank=True, max_length=1, null=True)),
                ('grade3', models.CharField(blank=True, max_length=1, null=True)),
                ('grade4', models.CharField(blank=True, max_length=1, null=True)),
                ('grade5', models.CharField(blank=True, max_length=1, null=True)),
                ('grade6', models.CharField(blank=True, max_length=1, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='result.department')),
                ('module1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module1_results', to='result.courses')),
                ('module2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module2_results', to='result.courses')),
                ('module3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module3_results', to='result.courses')),
                ('module4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module4_results', to='result.courses')),
                ('module5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module5_results', to='result.courses')),
                ('module6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module6_results', to='result.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.student')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.faculty'),
        ),
    ]
