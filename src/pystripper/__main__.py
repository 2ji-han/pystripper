from pathlib import Path
import click
import pystripper


@click.group()
def cli(): ...


@cli.command()
@click.option(
    "--input",
    "-i",
    type=click.Path(exists=True, dir_okay=False),
    required=True,
    help="Path to the input file.",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(dir_okay=False),
    required=True,
    help="Path to the output file.",
)
def strip(input: str, output: str):
    """Strip the input file and save it to the output file."""
    input_path = Path(input)
    output_path = Path(output)

    if not input_path.is_file():
        click.echo(f"Input file {input} does not exist.")
        return

    if output_path.exists():
        click.echo(f"Output file {output} already exists.")
        return

    pystripper.strip(input_path, output_path)
    click.echo(f"Stripped file saved to {output}")


@cli.command()
@click.option(
    "--path",
    "-p",
    "--input",
    "-i",
    type=click.Path(exists=True, dir_okay=True),
    required=True,
    help="Path to the input directory.",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(dir_okay=True),
    required=True,
    help="Path to the output directory.",
)
def strip_dir(path: str, output: str):
    """Strip all files in the input directory and save them to the output directory."""
    input_path = Path(path)
    output_path = Path(output)

    if not input_path.is_dir():
        click.echo(f"Input directory {path} does not exist.")
        return

    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)

    pystripper.strip_dir(input_path, output_path)
    click.echo(f"Stripped files saved to {output}")


if __name__ == "__main__":
    cli()
