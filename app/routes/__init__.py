from flask import Blueprint

# 创建蓝图
main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__, url_prefix='/auth')

# 导入路由处理函数
from . import main_routes, auth_routes 