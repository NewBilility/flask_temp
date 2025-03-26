from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from config import Config

# 初始化扩展
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
admin = Admin(name='后台管理系统', template_mode='bootstrap4')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    
    # 设置登录视图
    login_manager.login_view = 'auth.login'
    login_manager.login_message = '请先登录'
    login_manager.login_message_category = 'info'

    # 注册蓝图
    from app.routes import main, auth
    app.register_blueprint(main)
    app.register_blueprint(auth)

    # 创建数据库表
    with app.app_context():
        db.create_all()

    return app 