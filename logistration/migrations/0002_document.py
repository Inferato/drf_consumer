# Generated by Django 4.2.10 on 2024-03-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documets/')),
            ],
        ),
    ]
