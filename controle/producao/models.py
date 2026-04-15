from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nome}"


class OrdemProducao(models.Model):
    STATUS_CHOICES = [
        ("aberta", "Aberta"),
        ("em_producao", "Em produção"),
        ("finalizada", "Finalizada"),
        ("cancelada", "Cancelada"),
    ]

    numero = models.CharField(max_length=50, unique=True)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="ordens")
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_prevista = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="aberta")
    observacoes = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"OP {self.numero} - {self.produto}"


class Relacao(models.Model):
    nome = models.CharField(max_length=120)
    criada_em = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False)
    previsao_data = models.DateField(null=True, blank=True)
    liberacao_producao_data = models.DateField(null=True, blank=True)
    # Litros inferidos do texto → m³ = litros / este divisor (vazio = settings.PRODUCAO_LITROS_PARA_M3_DIVISOR).
    litros_divisor_m3 = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.nome

    @property
    def progresso_itens_ok(self) -> float:
        total = self.itens.count()
        if total == 0:
            return 0.0
        ok = self.itens.filter(ok=True).count()
        return (ok / total) * 100.0

    @property
    def progresso_quantidade_ok(self) -> float:
        itens = self.itens.all()
        total = 0.0
        ok = 0.0
        for item in itens:
            q = float(item.quantidade or 0)
            total += q
            if item.ok:
                ok += q
        if total <= 0:
            return 0.0
        return (ok / total) * 100.0

    @property
    def pedidos_distintos(self) -> list[str]:
        vals = (
            self.itens.exclude(pedido_numero="")
            .exclude(pedido_numero__isnull=True)
            .values_list("pedido_numero", flat=True)
        )
        # Normaliza em memória para colapsar variantes como "123 " e " 123".
        normalizados = {str(v).strip() for v in vals if str(v or "").strip()}
        return sorted(normalizados)

    @property
    def pedidos_subtitulo(self) -> str:
        peds = self.pedidos_distintos
        if not peds:
            return ""
        show = peds[:5]
        txt = ", ".join(show)
        if len(peds) > 5:
            txt += f" (+{len(peds) - 5})"
        return txt


class RelacaoItem(models.Model):
    relacao = models.ForeignKey(Relacao, on_delete=models.CASCADE, related_name="itens")
    indice = models.PositiveIntegerField(default=0)
    descricao = models.CharField(max_length=255, blank=True)
    codigo_produto = models.CharField(max_length=80, blank=True)
    ok = models.BooleanField(default=False)
    parcial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    odf = models.CharField(max_length=80, blank=True)
    pedido_numero = models.CharField(max_length=80, blank=True)
    data = models.DateField(null=True, blank=True)
    observacao = models.CharField(max_length=255, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["indice", "id"]

    def __str__(self) -> str:
        return f"{self.relacao.nome} #{self.indice}"


class Categoria(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    produtos = models.ManyToManyField(Produto, related_name="categorias", blank=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self) -> str:
        return self.nome


class FiltroPedido(models.Model):
    descricao = models.CharField(max_length=255, blank=True)
    cod_interno = models.CharField(max_length=120, blank=True)
    # Opcional: m³ por unidade (ex.: cubagem logística). Se preenchido, ignora extração do texto.
    volume_m3 = models.DecimalField(
        max_digits=14, decimal_places=6, null=True, blank=True
    )
    setor = models.CharField(max_length=120, blank=True)
    necessidade = models.CharField(max_length=120, blank=True)
    numero_pedido = models.CharField(max_length=80, blank=True)
    descricao_produto = models.CharField(max_length=255, blank=True)
    codigo_produto = models.CharField(max_length=120, blank=True)
    saldo_pedido = models.CharField(max_length=80, blank=True)
    fonte = models.CharField(max_length=120, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["numero_pedido", "id"]

    def __str__(self) -> str:
        return f"{self.numero_pedido} - {self.codigo_produto}"


class DiscoRazaoSocial(models.Model):
    ordem = models.PositiveIntegerField(default=0)
    cod = models.CharField(max_length=120, blank=True)
    razao_social = models.CharField(max_length=255, blank=True)
    segmento = models.CharField(max_length=120, blank=True)
    telefone = models.CharField(max_length=80, blank=True)
    bairro = models.CharField(max_length=120, blank=True)
    cidade = models.CharField(max_length=120, blank=True)
    uf = models.CharField(max_length=20, blank=True)
    col_h = models.CharField(max_length=255, blank=True)
    col_i = models.CharField(max_length=255, blank=True)
    origem = models.CharField(max_length=120, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordem", "id"]

    def __str__(self) -> str:
        return f"{self.cod} - {self.razao_social}"


class CacarolaMaquina(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self) -> str:
        return self.nome


class CacarolaProduto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    ciclo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self) -> str:
        return self.nome


class CacarolaRegistro(models.Model):
    uid = models.CharField(max_length=64, unique=True)
    data = models.DateField()
    turno = models.CharField(max_length=20, blank=True)
    maquina = models.CharField(max_length=120, blank=True)
    responsavel = models.CharField(max_length=120, blank=True)
    tipo_produto = models.CharField(max_length=20, blank=True)
    produto = models.CharField(max_length=255, blank=True)
    quantidade = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    odf = models.CharField(max_length=80, blank=True)
    inicio = models.TimeField(null=True, blank=True)
    fim = models.TimeField(null=True, blank=True)
    refeicao = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tempo = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    pecas_hora = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    paradas_min = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ciclo = models.DecimalField(max_digits=12, decimal_places=4, default=0)
    perdas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    material = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estampo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    polimento = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    refilador = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    rebite = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amassado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pintura = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data", "-id"]

    def __str__(self) -> str:
        return f"{self.data} · {self.maquina} · {self.produto}"
