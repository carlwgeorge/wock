import os
import pathlib
import click
from .utils import ContextObj


@click.group()
@click.option('--pkgname', help='[{}]'.format(pathlib.Path.cwd().name))
@click.option('--release', envvar='WOCK',
              help='[{}]'.format(os.environ.get('WOCK')))
@click.option('--architecture', default='x86_64', help='[x86_64]')
@click.pass_context
def cli(context, pkgname, release, architecture):
    ''' A stupid wrapper for mock. '''
    context.obj = ContextObj(pkgname, release, architecture)


@cli.command()
@click.pass_obj
def init(cobj):
    ''' Initialize a chroot. '''
    cobj.init()


@cli.command()
@click.pass_obj
def clean(cobj):
    ''' Purge the chroot. '''
    cobj.clean()


@cli.command()
@click.option('--just-srpm', is_flag=True, help='Only build the srpm.')
@click.pass_obj
def build(cobj, just_srpm):
    ''' Build an rpm inside the chroot. '''
    cobj.build(just_srpm)


@cli.command()
@click.argument('packages', nargs=-1, type=click.Path(exists=True))
@click.pass_obj
def install(cobj, packages):
    ''' Install rpm inside the chroot. '''
    cobj.install(packages)


@cli.command()
@click.argument('command', default='bash')
@click.pass_obj
def shell(cobj, command):
    ''' Run command interactively inside chroot. '''
    cobj.shell(command)
