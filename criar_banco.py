from photoshelf import database, app
from photoshelf.models import Usuario, Foto

with app.app_context():
    database.create_all()