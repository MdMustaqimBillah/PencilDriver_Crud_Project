# Generated by Django 5.0.3 on 2024-03-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician_Pedia', '0004_alter_album_id_alter_musician_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_ratings',
            new_name='ratings',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='album_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='musician',
            old_name='artist_age',
            new_name='age',
        ),
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]