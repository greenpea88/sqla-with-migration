import click

from app.db import engine, Session
from app.db.base import Base
from app.db.models import User


@click.group()
def cli():
    pass


@cli.add_command
@click.command()
def create_db():
    Base.metadata.create_all(engine)
    click.echo('created: database and tables')


@cli.add_command
@click.command()
@click.argument("username", required=True)
def create_user(username):
    user = User(username=username)
    with Session() as session:
        session.add(user)
        session.commit()
        click.echo(f'user: {user} created')


@cli.add_command
@click.command()
@click.option("--user-id", required=True)
@click.option("--new-username", required=True)
def update_user(user_id=None, new_username=None):
    with Session() as session:
        user = session.query(User).get(user_id)
        if not user:
            click.echo(f'user:{user_id} not found.')
            return

        user.username = new_username
        session.add(user)
        session.commit()
        click.echo(f'user: user:{user_id} updated.')


@cli.add_command
@click.command()
@click.option("--user-id", required=True)
def delete_user(user_id=None, ):
    with Session() as session:
        user = session.query(User).get(user_id)
        if not user:
            click.echo(f'user:{user_id} not found.')
            return

        session.delete(user)
        session.commit()
        click.echo(f'user: user:{user_id} deleted.')


if __name__ == "__main__":
    cli()
