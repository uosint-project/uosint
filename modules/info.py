from rich.console import Console
from rich.table import Table
from rich import print
table = Table(title="[cyan]User Open Source Intelligence[/cyan] [red][ [white]UOSINT[/white] [red]][/red]")

table.add_column("Flags", justify="center", style="cyan", no_wrap=True)
table.add_column("Description", justify="center", style="magenta")
table.add_column("IsRequired", justify="center", style="green")
table.add_column("API Required", justify="center", style="green")
table.add_column("API WebSite", justify="center", style="green")

table.add_row("-e[yellow] , [/yellow][cyan]--email",
              "[white]Sometime [bold magenta]USER[/bold magenta] write [bold magenta]Email[/bold magenta] in there [bold magenta]Bio[/bold magenta], in that case you will take that Email and use [cyan]-e[/cyan] command[yellow].[/yellow]",
              "Yes",
              "[green]Yes[/green]",
              "[red]No WebSite[/red]")

table.add_row("-u[yellow] , [/yellow][cyan]--username", "[white] Information will be collected from many website such as [bold green]Social Media[/bold green][yellow],[/yellow][bold green]Dating Platfrom[/bold green][yellow],[/yellow][bold green]Music Platfrom[/bold green][yellow],[/yellow][bold green]Porn[/bold green][yellow],[/yellow] etc[yellow].[/yellow]", "Yes", "[red]No[/red]", "[red]No WebSite[/red]")

table.add_row("-n[yellow] , [/yellow][cyan]--number",
              "[white]Sometime [bold magenta]USER[/bold magenta] write [bold magenta]Phone Number[/bold magenta] in there [bold magenta]Bio[/bold magenta], in that case you will take that phoneNumber and use [cyan]-n[/cyan] command[yellow].[/yellow]",
              "Yes", "[green]Yes[/green]",
              "[red]No WebSite[/red]")


console = Console()
console.print(table)