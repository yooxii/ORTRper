import sqlite3
import pandas as pd

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

def get_plans_db():
    if 'plansdb' not in g:
        g.plansdb = sqlite3.connect(
            database=current_app.config['PLANS_DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES    
        )
        g.plansdb.row_factory = sqlite3.Row
        
        return g.plansdb

def close_db(e=None):
    ortdb = g.pop('ortdb', None)
    plansdb = g.pop('plansdb', None)
    
    if ortdb is not None:
        ortdb.close
    if plansdb is not None:
        plansdb.close

def init_ort_db():
    ortdb = get_ort_db()
    
    with current_app.open_resource('schema.sql') as f:
        ortdb.executescript(f.read().decode('utf-8'))

def init_plans_db():
    plansdb = get_plans_db()
    
    with current_app.open_resource('plans.sql') as f:
        plansdb.executescript(f.read().decode('utf-8'))
    
def init_ti_db():
    tidb = get_plans_db()
    
    with current_app.open_resource('TI.sql') as f:
        tidb.executescript(f.read().decode('utf-8'))
    custcode = pd.read_csv(current_app.config['ORT_PLANS']["CustCode"])
    for i in range(len(custcode)):
        tidb.execute("INSERT INTO CustCode (Code, Customer, product_type, full_product_type) VALUES (?,?,?,?)", (custcode.iloc[i,0], custcode.iloc[i,1], custcode.iloc[i,2], custcode.iloc[i,3]))
        tidb.commit()
    ProductType = pd.read_csv(current_app.config['ORT_PLANS']["ProductType"])
    for i in range(len(ProductType)):
        tidb.execute("INSERT INTO ProductType (Code, Type) VALUES (?,?)", (ProductType.iloc[i,0], ProductType.iloc[i,1]))
        tidb.commit()
    TestItems = pd.read_csv(current_app.config['ORT_PLANS']["TestItems"])
    for i in range(len(TestItems)):
        tidb.execute("INSERT INTO TestItems (TestItem, TestPeriod, Owner, Dispose, Remark) VALUES (?,?,?,?,?)", (TestItems.iloc[i,1], TestItems.iloc[i,2], TestItems.iloc[i,3], TestItems.iloc[i,4], TestItems.iloc[i,5]))
        tidb.commit()
    checkoutsTIs = pd.read_csv(current_app.config['ORT_PLANS']["checkoutsTIs"])
    for i in range(len(checkoutsTIs)):
        tidb.execute("INSERT INTO CheckoutTIs (TI) VALUES (?)", (checkoutsTIs.iloc[i,0],))
        tidb.commit()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_ort_db_command)
    app.cli.add_command(init_plans_db_command)
    app.cli.add_command(init_ti_db_command)

@click.command('init-ort-db')
def init_ort_db_command():
    init_ort_db()
    click.echo('Initialized the ORT database.')

@click.command('init-plans-db')
def init_plans_db_command():
    init_plans_db()
    click.echo('Initialized the Plans database.')
    
@click.command('init-ti-db')
def init_ti_db_command():
    init_ti_db()
    click.echo('Initialized the TI database.')
