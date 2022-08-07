# Generated by Django 3.2.4 on 2021-07-19 18:28

import uuid

import django.db.models.expressions
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('profile_completed', models.BooleanField(default=False)),
                ('about_self', models.TextField(blank=True, max_length=512)),
                ('specialization', models.TextField(blank=True, max_length=256)),
                ('expected_min_mentorship_duration', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('expected_max_mentorship_duration', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_accepting_mentorship_requests', models.BooleanField(default=True)),
                ('other_responsibility', models.TextField(blank=True, max_length=512)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('accepted_mentee_types', models.ManyToManyField(blank=True, to='mentee.MenteeDesignation')),
            ],
        ),
        migrations.CreateModel(
            name='MentorDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('label', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MentorDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('label', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MentorDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('label', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MentorResponsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.TextField(max_length=256, unique=True)),
            ],
            options={
                'verbose_name_plural': 'MentorResponsibilities',
            },
        ),
        migrations.CreateModel(
            name='MentorResearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('organization', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('details', models.TextField(blank=True, max_length=512)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='researches',
                                             to='mentor.mentor')),
            ],
            options={
                'verbose_name_plural': 'MentorResearches',
                'ordering': [
                    django.db.models.expressions.OrderBy(django.db.models.expressions.F('end_date'), descending=True,
                                                         nulls_last=True), '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='MentorEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('qualification', models.CharField(max_length=128)),
                ('organization', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('details', models.TextField(blank=True, max_length=512)),
                ('link', models.URLField(blank=True)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations',
                                             to='mentor.mentor')),
            ],
            options={
                'ordering': [
                    django.db.models.expressions.OrderBy(django.db.models.expressions.F('end_date'), descending=True,
                                                         nulls_last=True), '-start_date'],
            },
        ),
        migrations.AddField(
            model_name='mentor',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                    related_name='mentors_with_department', to='mentor.mentordepartment'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                    related_name='mentors_with_designation', to='mentor.mentordesignation'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                    related_name='mentors_with_discipline', to='mentor.mentordiscipline'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='responsibilities',
            field=models.ManyToManyField(blank=True, to='mentor.MentorResponsibility'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]