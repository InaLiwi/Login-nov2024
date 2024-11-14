from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('usuario_nombre', models.CharField(max_length=100, verbose_name='Usuario')),
                ('usuario_password', models.CharField(max_length=100,verbose_name='Password')),
            ],
        ),
    ]
