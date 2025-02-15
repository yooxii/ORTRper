import os
from flask import Flask, render_template

def create_app(test_config=None):
    app =Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        ORT_DATABASE=os.path.join(app.instance_path, 'ort.sqlite'),
        PLANS_DATABASE=os.path.join(app.instance_path, 'plans.sqlite'),
        ORT_SCHEDULE=os.path.join(app.instance_path, 'Y2025 ORT Test Schedule.xlsx')
    )
    
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/ort/<string:page_name>')
    def ort(page_name):
        return render_template(template_name_or_list='ort/' + page_name + '.html')
    
    from . import db, auth, plans, report
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(plans.bp)
    app.register_blueprint(report.bp)

    return app