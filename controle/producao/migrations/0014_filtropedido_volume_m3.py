from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0013_relacao_datas_planejamento"),
    ]

    operations = [
        migrations.AddField(
            model_name="filtropedido",
            name="volume_m3",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=14, null=True
            ),
        ),
    ]
