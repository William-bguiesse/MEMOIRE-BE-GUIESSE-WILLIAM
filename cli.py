import click

@click.group()
def cli():
    pass

@cli.command()
def read():
    """Lecture du fichier importé"""
    pass

@cli.command()
def convert():
    """Conversion du fichier importé"""
    pass

@cli.command()
def generate():
    """Génération du site statique HTML"""
    pass

@cli.command()
def serve():
    """Lancement du serveur web"""
    pass

if __name__ == '__main__':
    cli()