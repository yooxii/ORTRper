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

@bp.route('/checkouts', methods=('GET', 'POST'))
def Checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    
    return render_template('plans/Checkouts.html', checkoutsPeek=db_checkouts)

@bp.route('/checkouts/import_checkouts', methods=('GET', 'POST'))
def import_checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    
    return render_template('plans/Checkouts.html', checkoutsPeek=db_checkouts)

@bp.route('/checkouts/export_checkouts', methods=('GET', 'POST'))
def export_checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    
    return render_template('plans/Checkouts.html', checkoutsPeek=db_checkouts)

@bp.route('/checkouts/edit_checkouts', methods=('GET', 'POST'))
def edit_checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    tis = db.execute('SELECT * FROM CheckoutTIs').fetchall()
    if request.method == 'POST':
        ckouts = request.form.to_dict(flat=False)  # 使用to_dict(flat=False)获取表单数据为字典列表

        for checkout in zip(*ckouts.values()):  # 使用zip(*checkouts.values())同时迭代多个列表
            checkout_no = checkout[1]
            db_checkout = db.execute('SELECT * FROM TCheckouts WHERE checkout_no = ?', (checkout_no,)).fetchone()
            if db_checkout:
                # 去掉checkout_no
                checkout_ = (checkout[0],) + checkout[2:]
                db.execute('UPDATE TCheckouts SET checkout_date = ?, PartNo = ?, checkout_qty = ?, TestItem = ?, SN = ?, DC = ?, REV = ?, Work_Order = ?, Remarks = ? WHERE checkout_no = ?', checkout_ + (checkout_no,))
                db.commit()
                flash('Checkout with number {} updated successfully'.format(checkout_no))
            else:
                try:
                    print(checkout)
                    db.execute('INSERT INTO TCheckouts (checkout_date, checkout_no, PartNo, checkout_qty, TestItem, SN, DC, REV, Work_Order, Remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', checkout)
                    db.commit()
                    flash('Checkout with number {} submitted successfully'.format(checkout_no))
                except Exception as e:
                    flash('Error submitting checkout with number {}: {}'.format(checkout_no, str(e)))
                    db.rollback()  # 回滚事务以防止数据不一致
        return redirect(url_for('.Checkouts'))
    return render_template('plans/checkouts_edit.html', checkoutsPeek=db_checkouts, testItems=tis)

@bp.route('/checkouts/delete', methods=('POST',))
def delete():
    db = get_plans_db()
    checkout_no = request.form.get('checkout_no')  # 使用get方法获取表单数据，防止键不存在时报错

    if not checkout_no:
        flash('Checkout number is required')
        return redirect(url_for('plans.Checkouts'))

    try:
        db.execute('DELETE FROM TCheckouts WHERE checkout_no = ?', (checkout_no,))
        db.commit()
        flash('Checkout with number {} deleted successfully'.format(checkout_no))
    except Exception as e:
        db.rollback()  # 回滚事务以防止数据不一致
        flash('Error deleting checkout with number {}: {}'.format(checkout_no, str(e)))
    return redirect(url_for('plans.checkouts'))
