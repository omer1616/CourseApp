# Generated by Django 4.1.4 on 2023-02-16 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_comment_evulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='evulation',
            field=models.CharField(choices=[('1', 'Kötü'), ('2', 'Eh İşte'), ('3', 'İdare Eder'), ('4', 'İyi'), ('5', 'Çok iyi')], default=5, max_length=25),
        ),
    ]
