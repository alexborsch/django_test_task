# Generated by Django 3.2.13 on 2022-06-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220614_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productoptions'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productimages'),
        ),
    ]
