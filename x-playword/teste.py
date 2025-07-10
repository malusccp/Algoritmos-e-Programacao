from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.box import ROUNDED
from rich.padding import Padding

console = Console()

def exibir_menu(lista):
    console.clear()

    titulo = Text("🎮 PLAY NUMBERS", style="bold white on blue", justify="center")
    painel_titulo = Panel(titulo, style="bold blue", padding=(1, 10), box=ROUNDED)
    console.print(painel_titulo)


    if lista:
        vetor_str = ", ".join(map(str, lista))
        painel_vetor = Panel(
            f"[green]📌 Vetor atual:[/green] [white]{vetor_str}[/white]",
            style="cyan",
            padding=(1, 2),
            box=ROUNDED
        )
    else:
        painel_vetor = Panel(
            "[yellow]⚠️ Vetor ainda não inicializado.[/yellow]",
            style="red",
            box=ROUNDED
        )

    console.print(painel_vetor)

    # Tabela com as opções
    tabela = Table(title="🔽 Menu de Opções", box=ROUNDED, title_style="bold green", show_lines=True)
    tabela.add_column("🔢 Nº", justify="center", style="bold cyan")
    tabela.add_column("📋 Ação", style="bold white")

    opcoes = [
        ("1", "📥 Inicializar Vetor Numérico"),
        ("2", "📄 Mostrar Todos os Valores"),
        ("3", "♻️ Resetar Vetor"),
        ("4", "🔎 Ver Quantidade de Itens"),
        ("5", "📉 Ver Menor e Maior Valores"),
        ("6", "➕ Somatório dos Valores"),
        ("7", "📊 Média dos Valores"),
        ("8", "✅ Mostrar Valores Positivos"),
        ("9", "❌ Mostrar Valores Negativos"),
        ("10", "🛠️ Atualizar Todos os Valores"),
        ("11", "➕ Adicionar Novos Valores"),
        ("12", "🗑️ Remover por Valor Exato"),
        ("13", "📍 Remover por Posição"),
        ("14", "✏️ Editar Valor por Posição"),
        ("15", "💾 Salvar em Arquivo"),
        ("0", "[red]🚪 Sair[/red]"),
    ]

    for numero, descricao in opcoes:
        tabela.add_row(numero, descricao)

    console.print(tabela)

    # Rodapé
    rodape = Text("Digite o número da opção desejada e pressione Enter.", justify="center", style="dim")
    console.print(Padding(rodape, (1, 0, 1, 0)))
