import functools
import pandas as pd
import openpyxl as xl

from flask import (
    current_app, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_ort_db


bp= Blueprint('plans', __name__, url_prefix='/plans')

@bp.route('/schedule', methods=('GET', 'POST'))
def schedule():
    # wb = xl.load_workbook(current_app.config['ORT_SCHEDULE'])
    # sn= wb.sheetnames[1]
    df = pd.read_excel(current_app.config['ORT_SCHEDULE'], sheet_name=0, na_values='NA', keep_default_na=True)
    sn = df.to_html()
    return render_template('plans/schedule.html', sheetname=sn)

@bp.route('/lingyong', methods=('GET', 'POST'))
def lingyong():
    return render_template('plans/lingyong.html')