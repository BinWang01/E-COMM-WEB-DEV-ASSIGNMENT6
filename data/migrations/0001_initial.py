# Generated by Django 4.2.4 on 2023-11-03 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(help_text='The name of the College.', max_length=100)),
                ('college_website', models.URLField(blank=True, help_text='The website of the College.', null=True)),
                ('college_description', models.CharField(blank=True, help_text='The description of the College.', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(help_text='The number of the Course.', max_length=100)),
                ('course_name', models.CharField(help_text='The name of the Course.', max_length=100)),
                ('course_description', models.CharField(blank=True, help_text='The description of the Course.', max_length=200, null=True)),
                ('total_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(help_text='The name of the Degree.', max_length=100)),
                ('degree_description', models.CharField(blank=True, help_text='The description of the Degree.', max_length=200, null=True)),
                ('degree_website', models.URLField(blank=True, help_text='The website of the Degree.', null=True)),
                ('online_degree', models.BooleanField(default=False)),
                ('total_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(help_text='The name of the Department.', max_length=100)),
                ('department_description', models.CharField(blank=True, help_text='The description of the Department.', max_length=200, null=True)),
                ('department_website', models.URLField(blank=True, help_text='The website of the Department.', null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.college')),
            ],
        ),
        migrations.CreateModel(
            name='DegreeCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal_year', models.IntegerField()),
                ('is_optional', models.BooleanField(default=False)),
                ('is_core', models.BooleanField()),
                ('is_degree', models.BooleanField()),
                ('is_major', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.course')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.degree')),
            ],
        ),
        migrations.AddField(
            model_name='degree',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.department'),
        ),
    ]
