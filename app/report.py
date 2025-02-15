import functools
import openpyxl as xl

from flask import (
    current_app, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db


bp= Blueprint('report', __name__, url_prefix='/report')

@bp.route('/amz', methods=('GET', 'POST'))
def amz():
    return render_template('report/amz.html')

@bp.route('/EMI168', methods=('GET', 'POST'))
def EMI168():
    return render_template('report/EMI168.html')