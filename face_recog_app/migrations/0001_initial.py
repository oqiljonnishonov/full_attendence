# Generated by Django 4.2.11 on 2024-04-08 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Group Name')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Student Name')),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_recog_app.groups', verbose_name='group_id')),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Added time')),
                ('status', models.BooleanField(default=False, help_text='if it is true , that means user is here')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_recog_app.students', verbose_name='user_id')),
            ],
        ),
    ]
