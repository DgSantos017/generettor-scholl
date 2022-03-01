# Generated by Django 3.2.8 on 2022-02-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
        ('turmas', '0002_auto_20220228_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerturmas',
            name='professores',
        ),
        migrations.AddField(
            model_name='registerturmas',
            name='materias',
            field=models.ManyToManyField(related_name='turmas', to='materias.RegisterMaterias'),
        ),
    ]
