# Generated by Django 3.0.2 on 2020-02-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('black_widow', '0007_auto_20200129_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webparsingjobmodel',
            name='_parsing_tags',
            field=models.CharField(choices=[('all_parse', 'All Tags'), ('relevant_parse', 'Relevant Tags (a, script, link, Form Tags, Meta Tags)'), ('form_parse', 'Form Tags (form, input, textarea, select, option)'), ('meta_parse', 'Meta Tags (meta, xmp)')], max_length=50),
        ),
    ]