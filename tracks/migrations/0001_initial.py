# Generated by Django 2.0.7 on 2020-02-07 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en la cual se modifico el objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en la cual se modifico el objeto', verbose_name='modified at')),
                ('number_track', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveSmallIntegerField()),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/tracks/', verbose_name='Archivo de sonido')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Album')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]