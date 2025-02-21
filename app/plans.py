import datetime
import os
from io import BytesIO
import pandas as pd
import numpy as np
import openpyxl as xl

from flask import (
    current_app, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from app.db import get_plans_db

from rich import inspect

bp= Blueprint('plans', __name__, url_prefix='/plans')

@bp.route('/schedule', methods=('GET', 'POST'))
def schedule():
    
    return render_template('plans/schedule.html')

@bp.route('/checkouts', methods=('GET', 'POST'))
def Checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    
    return render_template('plans/Checkouts.html', checkoutsPeek=db_checkouts, rd_or_rq='readonly')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def conver_excel_date(x):
    try:
        return pd.to_datetime('1899-12-30') + pd.to_timedelta(x, unit='D')
    except:
        return x  # 如果转换失败，返回原始值

@bp.route('/checkouts/import_checkouts', methods=('GET', 'POST'))
def import_checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    
    if request.method == 'POST':
        # inspect(request)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        print(file.filename)
        
        if file and allowed_file(file.filename):
            excelFile = pd.ExcelFile(BytesIO(file.stream.read()))
            for sheet_name in excelFile.sheet_names:
                df = excelFile.parse(sheet_name,converters={0: conver_excel_date},skiprows=3)
                # 去掉空值大于1的行
                df = df.dropna(thresh=9)
                # 不取代列名
                df.columns = df.iloc[0]
                # 从db里读取所有列名作为df的列名
                index = db.execute('PRAGMA table_info(TCheckouts)').fetchall()
                index = [i[1] for i in index]
                df = df.reindex(columns=index)
                inspect(df)
                df.to_sql('TCheckouts', db, if_exists='append', index=False)
                # for row in df.itertuples():
                #     try:
                #         # 将row转化为只有值的元组
                #         checkout_ = tuple(row[1:])
                #         inspect(checkout_)
                #         db.execute('INSERT INTO TCheckouts (checkout_date, checkout_no, PartNo, checkout_qty, TestItem, SN, DC, REV, Work_Order, Remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', checkout_)
                #         db.commit()
                #     except Exception as e:
                #         flash('Error importing checkouts: {}'.format(str(e)))
                #         db.rollback()  # 回滚事务以防止数据不一致
    
    return render_template('plans/Checkouts.html', checkoutsPeek=db_checkouts, rd_or_rq='readonly')

@bp.route('/checkouts/export_checkouts', methods=('GET', 'POST'))
def export_checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    
    return render_template('plans/Checkouts.html', checkoutsPeek=db_checkouts, rd_or_rq='readonly')

@bp.route('/checkouts/edit_checkouts', methods=('GET', 'POST'))
def edit_checkouts():
    db = get_plans_db()
    db_checkouts = db.execute('SELECT * FROM TCheckouts').fetchall()
    tis = db.execute('SELECT * FROM CheckoutTIs').fetchall()
    if request.method == 'POST':
        inspect(request)
        ckouts = request.form.to_dict(flat=False)  # 使用to_dict(flat=False)获取表单数据为字典列表

        for checkout in zip(*ckouts.values()):  # 使用zip(*checkouts.values())同时迭代多个列表
            checkout_no = checkout[2]
            db_checkout = db.execute('SELECT * FROM TCheckouts WHERE checkout_no = ?', (checkout_no,)).fetchone()
            if db_checkout:
                # 去掉checkout_no
                checkout_ = checkout[0:2] + checkout[3:]
                db.execute('UPDATE TCheckouts SET id = ?, checkout_date = ?, PartNo = ?, checkout_qty = ?, TestItem = ?, SN = ?, DC = ?, REV = ?, Work_Order = ?, Remarks = ? WHERE checkout_no = ?', checkout_ + (checkout_no,))
                db.commit()
                flash('Checkout with number {} updated successfully'.format(checkout_no))
            else:
                try:
                    db.execute('INSERT INTO TCheckouts (checkout_date, checkout_no, PartNo, checkout_qty, TestItem, SN, DC, REV, Work_Order, Remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', checkout[1:])
                    db.commit()
                    flash('Checkout with number {} submitted successfully'.format(checkout_no))
                except Exception as e:
                    flash('Error submitting checkout with number {}: {}'.format(checkout_no, str(e)))
                    db.rollback()  # 回滚事务以防止数据不一致
        return redirect(url_for('.Checkouts'))
    return render_template('plans/checkouts_edit.html', checkoutsPeek=db_checkouts, testItems=tis, rd_or_rq='required')

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
