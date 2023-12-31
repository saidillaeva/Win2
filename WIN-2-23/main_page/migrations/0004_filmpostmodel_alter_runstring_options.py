# Generated by Django 4.2.7 on 2023-11-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_remove_runstring_title2'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Enter your film name')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='films/')),
                ('cost', models.PositiveIntegerField()),
                ('genre', models.CharField(choices=[('Horror', 'Horror'), ('Comedy', 'Comedy')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='runstring',
            options={'verbose_name': 'Бегущую строку', 'verbose_name_plural': 'Бегущие строки'},
        ),
    ]
