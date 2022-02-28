# Generated by Django 3.2.8 on 2022-02-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastrarProfessores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_professor', models.CharField(max_length=255, unique=True)),
                ('materias', models.ManyToManyField(related_name='professores', to='materias.RegisterMaterias')),
            ],
        ),
    ]
