# Generated by Django 4.0.4 on 2022-06-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weebs', '0010_manhua_categoryimage_manhua_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='manhua',
            name='type',
            field=models.CharField(blank=True, max_length=23, null=True),
        ),
        migrations.AddField(
            model_name='manhwa',
            name='type',
            field=models.CharField(blank=True, max_length=23, null=True),
        ),
    ]
