from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0015_relacao_litros_divisor_m3"),
    ]

    operations = [
        migrations.AddField(
            model_name="relacaoitem",
            name="observacao",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
