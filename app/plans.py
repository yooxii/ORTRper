import functools
import pandas as pd
import openpyxl as xl

from flask import (
    current_app, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_plans_db


bp= Blueprint('plans', __name__, url_prefix='/plans')

@bp.route('/schedule', methods=('GET', 'POST'))
def schedule():
    # wb = xl.load_workbook(current_app.config['ORT_SCHEDULE'])
    # sn= wb.sheetnames[1]
    df = pd.read_excel(current_app.config['ORT_SCHEDULE'],skiprows=2, sheet_name=0, na_values='NA', keep_default_na=True)
    sn = df.to_html()
    return render_template('plans/schedule.html', sheetname=sn)

@bp.route('/Claims', methods=('GET', 'POST'))
def Claims():
    db = get_plans_db()
    claims = db.execute('SELECT * FROM claims').fetchall()
    if request.method == 'POST':
        claim = dict(request.form)
        db.execute('INSERT INTO Claims (claim_date, claim_no, PartNo, claim_qty, TestItem, SN, DC, REV, Work_Order, Remarks) VALUES (?,?,?,?,?,?,?,?,?,?)', (claim['claim_date'], claim['claim_no'], claim['PartNo'], claim['claim_qty'], claim['TestItem'], claim['SN'], claim['DC'], claim['REV'], claim['Work_Order'], claim['Remarks']))
        db.commit()
        claims = db.execute('SELECT * FROM Claims').fetchall()
        flash('Claim submitted successfully')
        return redirect(url_for('plans.Claims'))
    return render_template('plans/Claims.html', claimsPeek=claims)