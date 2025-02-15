import sqlite3

import click
from flask import current_app, g

def get_ort_db():
    if 'ortdb' not in g:
        g.ortdb = sqlite3.connect(
            database=current_app.config['ORT_DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES    
        )
        g.ortdb.row_factory = sqlite3.Row
        
        return g.ortdb
    
def close_db(e=None):
    ortdb = g.pop('ortdb', None)
    
    if ortdb is not None:
        ortdb.close

def init_ort_db():
    ortdb = get_ort_db()
    
    with current_app.open_resource('schema.sql') as f:
        ortdb.executescript(f.read().decode('utf-8'))
        
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
        
@click.command('init-ort-db')
def init_db_command():
    init_ort_db()
    click.echo('Initialized the ORT database.')