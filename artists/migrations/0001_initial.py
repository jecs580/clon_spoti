# Generated by Django 2.0.7 on 2020-02-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en la cual se modifico el objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en la cual se modifico el objeto', verbose_name='modified at')),
                ('name', models.CharField(error_messages={'unique': 'Nombre de artista ya existente'}, max_length=64, unique=True, verbose_name='Nombre Artistico')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description del artista')),
                ('image', models.ImageField(blank=True, null=True, upload_to='artist/pictures/', verbose_name='foto del Artista')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
