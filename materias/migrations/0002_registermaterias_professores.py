# Generated by Django 3.2.8 on 2022-03-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0002_remove_cadastrarprofessores_materias'),
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermaterias',
            name='professores',
            field=models.ManyToManyField(related_name='materias', to='professores.CadastrarProfessores'),
        ),
    ]
