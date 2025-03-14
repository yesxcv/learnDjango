# Generated by Django 5.1.6 on 2025-03-13 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfLearn', '0002_alter_article_options_article_like_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Published'), ('d', 'Draft')], default='p', max_length=1, null=True, verbose_name='Status (*)'),
        ),
    ]
