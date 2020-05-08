from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ccapp.config import Config

db = SQLAlchemy()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from ccapp.queues.routes import queue
    from ccapp.agents.routes import agent
    from ccapp.members.routes import member
    from ccapp.errors.handlers import errors
    from ccapp.callreport.avgcall.routes import avg
    from ccapp.callreport.graph.routes import graph
    from ccapp.callreport.kpi.routes import kpi
    from ccapp.cdrs.routes import cdr
    from ccapp.popup.repair.routes import pop

    app.register_blueprint(queue)
    app.register_blueprint(agent)
    app.register_blueprint(member)
    app.register_blueprint(errors)
    app.register_blueprint(avg)
    app.register_blueprint(graph)
    app.register_blueprint(kpi)
    app.register_blueprint(cdr)
    app.register_blueprint(pop)

    return app
