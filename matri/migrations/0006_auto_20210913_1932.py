# Generated by Django 3.2.4 on 2021-09-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matri', '0005_auto_20210913_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='caste',
            field=models.CharField(choices=[('Brahmin', 'Brahmin'), ('Newar', 'Newar'), ('Rai', 'Rai'), ('Tamang', 'Tamang')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('PHD', 'PHD'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(choices=[('Businessman', 'Businessman'), ('Teacher', 'Teacher'), ('Software Developer', 'Software Developer'), ('Banker', 'Banker')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='salary',
            field=models.CharField(choices=[('20000-30000', '20000-30000'), ('30000-40000', '30000-40000'), ('less than 20000', 'less than 20000'), ('40000 above', '40000 above')], max_length=200),
        ),
        migrations.AlterField(
            model_name='requestprofile',
            name='caste',
            field=models.CharField(choices=[('Brahmin', 'Brahmin'), ('Newar', 'Newar'), ('Rai', 'Rai'), ('Tamang', 'Tamang')], max_length=200),
        ),
        migrations.AlterField(
            model_name='requestprofile',
            name='education',
            field=models.CharField(choices=[('PHD', 'PHD'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters')], max_length=200),
        ),
        migrations.AlterField(
            model_name='requestprofile',
            name='salary',
            field=models.CharField(choices=[('20000-30000', '20000-30000'), ('30000-40000', '30000-40000'), ('less than 20000', 'less than 20000'), ('40000 above', '40000 above')], max_length=200),
        ),
    ]
