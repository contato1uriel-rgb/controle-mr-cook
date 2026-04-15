from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0005_filtropedido"),
    ]

    operations = [
        migrations.AddField(
            model_name="filtropedido",
            name="cod_interno",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="filtropedido",
            name="descricao",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="filtropedido",
            name="necessidade",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="filtropedido",
            name="setor",
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
