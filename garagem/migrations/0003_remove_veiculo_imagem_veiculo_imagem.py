# Generated by Django 4.2.4 on 2023-08-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0002_alter_modelo_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='imagem',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='imagem',
            field=models.ManyToManyField(related_name='+', to='uploader.image'),
        ),
    ]
