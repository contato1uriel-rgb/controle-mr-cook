from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0006_filtropedido_layout_cols"),
    ]

    operations = [
        migrations.AddField(
            model_name="relacaoitem",
            name="pedido_numero",
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
