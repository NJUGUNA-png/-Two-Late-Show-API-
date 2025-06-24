from models import db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from flask import Flask
from server.app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    guest1 = Guest(name="Roddy Rich", occupation="Actor")
    guest2 = Guest(name="Travis Scott", occupation="Singer")
    
    ep1 = Episode(date="2023-06-01", number=101)
    ep2 = Episode(date="2023-06-02", number=102)

    db.session.add_all([guest1, guest2, ep1, ep2])
    db.session.commit()

    app1 = Appearance(rating=5, guest_id=guest1.id, episode_id=ep1.id)
    app2 = Appearance(rating=4, guest_id=guest2.id, episode_id=ep2.id)

    db.session.add_all([app1, app2])
    db.session.commit()