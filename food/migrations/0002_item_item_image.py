# Generated by Django 4.2.16 on 2024-11-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://worldfoodtour.co.uk/wp-content/uploads/2013/06/neptune-placeholder-48.jpg', max_length=1000),
        ),
    ]