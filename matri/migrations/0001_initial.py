# Generated by Django 3.2.4 on 2021-09-13 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('phone', models.IntegerField(unique=True)),
                ('details', models.TextField()),
                ('salary', models.CharField(choices=[('30000-40000', '30000-40000'), ('20000-30000', '20000-30000'), ('40000 above', '40000 above'), ('less than 20000', 'less than 20000')], max_length=200)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('education', models.CharField(choices=[('PHD', 'PHD'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters')], max_length=200)),
                ('caste', models.CharField(choices=[('Brahmin', 'Brahmin'), ('Newar', 'Newar'), ('Tamang', 'Tamang'), ('Rai', 'Rai')], max_length=200)),
                ('occupation', models.CharField(choices=[('Businessman', 'Businessman'), ('Banker', 'Banker'), ('Teacher', 'Teacher'), ('Software Developer', 'Software Developer')], max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('username', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=200)),
                ('age1', models.IntegerField()),
                ('age2', models.IntegerField()),
                ('salary', models.CharField(choices=[('30000-40000', '30000-40000'), ('20000-30000', '20000-30000'), ('40000 above', '40000 above'), ('less than 20000', 'less than 20000')], max_length=200)),
                ('education', models.CharField(choices=[('PHD', 'PHD'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters')], max_length=200)),
                ('caste', models.CharField(choices=[('Brahmin', 'Brahmin'), ('Newar', 'Newar'), ('Tamang', 'Tamang'), ('Rai', 'Rai')], max_length=200)),
                ('phone', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='matri.profile')),
                ('username', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
