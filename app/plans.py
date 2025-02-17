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
    
    return render_template('plans/schedule.html')

@bp.route('/Claims', methods=('GET', 'POST'))
def Claims():
    db = get_plans_db()
    db_claims = db.execute('SELECT * FROM claims').fetchall()
    
    if request.method == 'POST':
        claims = request.form.to_dict(flat=False)  # 使用to_dict(flat=False)获取表单数据为字典列表

        for claim in zip(*claims.values()):  # 使用zip(*claims.values())同时迭代多个列表
            claim_no = claim[1]
            db_claim = db.execute('SELECT * FROM Claims WHERE claim_no = ?', (claim_no,)).fetchone()
            if db_claim:
                flash('Claim with number {} already exists'.format(claim_no))
            else:
                try:
                    db.execute('INSERT INTO Claims (claim_date, claim_no, PartNo, claim_qty, TestItem, SN, DC, REV, Work_Order, Remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', claim)
                    db.commit()
                    flash('Claim with number {} submitted successfully'.format(claim_no))
                except Exception as e:
                    flash('Error submitting claim with number {}: {}'.format(claim_no, str(e)))
                    db.rollback()  # 回滚事务以防止数据不一致
        return redirect(url_for('plans.Claims'))
    
    return render_template('plans/Claims.html', claimsPeek=db_claims)
