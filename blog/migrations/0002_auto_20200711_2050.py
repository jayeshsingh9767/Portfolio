# Generated by Django 3.0.8 on 2020-07-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, to='category.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='highlights',
            field=models.TextField(help_text='Enter Phrase to be highlighted in Blog Post', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(help_text='Enter comma seperated String', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text='Enter Title', max_length=255, unique=True),
        ),
    ]