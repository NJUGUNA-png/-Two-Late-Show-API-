from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = int(data["rating"])
    if not 1 <= rating <= 5:
        return jsonify(error="Rating must be 1–5"), 400

    appearance = Appearance(
        rating=rating,
        guest_id=data["guest_id"],
        episode_id=data["episode_id"]
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify(message="Appearance added", id=appearance.id), 201