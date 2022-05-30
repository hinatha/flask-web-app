from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

# create_app関数を作成する
def create_app():
    # Flaskインスタンス生成
    app = Flask(__name__)
    # Appのconfig設定
    app.config.from_mapping(
        SECRET_KEY="dw4lfOk490387dEYW5",
        SQLALCHEMY_DATABASE_URI=
            f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHRMY_ECHO=True,
        WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f",
    )
    # SQLAlchemyとAppの連携
    db.init_app(app)

    # MigrateとAppの連携
    Migrate(app, db)
    csrf.init_app(app)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app