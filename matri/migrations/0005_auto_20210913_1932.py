# Generated by Django 3.2.4 on 2021-09-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matri', '0004_auto_20210913_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestprofile',
            name='phone',
        ),
        migrations.AlterField(
            model_name='profile',
            name='caste',
            field=models.CharField(choices=[('Tamang', 'Tamang'), ('Newar', 'Newar'), ('Rai', 'Rai'), ('Brahmin', 'Brahmin')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('PHD', 'PHD'), ('Masters', 'Masters')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(choices=[('Software Developer', 'Software Developer'), ('Teacher', 'Teacher'), ('Businessman', 'Businessman'), ('Banker', 'Banker')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.CharField(choices=[('30000-40000', '30000-40000'), ('less than 20000', 'less than 20000'), ('20000-30000', '20000-30000'), ('40000 above', '40000 above')], max_length=200),
        ),
        migrations.AlterField(
            model_name='requestprofile',
            name='caste',
            field=models.CharField(choices=[('Tamang', 'Tamang'), ('Newar', 'Newar'), ('Rai', 'Rai'), ('Brahmin', 'Brahmin')], max_length=200),
        ),
        migrations.AlterField(
            model_name='requestprofile',
            name='education',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('PHD', 'PHD'), ('Masters', 'Masters')], max_length=200),
        ),
        migrations.AlterField(
            model_name='requestprofile',
            name='salary',
            field=models.CharField(choices=[('30000-40000', '30000-40000'), ('less than 20000', 'less than 20000'), ('20000-30000', '20000-30000'), ('40000 above', '40000 above')], max_length=200),
        ),
    ]
