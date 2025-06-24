from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models import db

episode_bp = Blueprint("episodes", __name__)


@episode_bp.route("/", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {
            "id": e.id,
            "date": e.date,
            "number": e.number,
            "appearances": [
                {
                    "guest_id": a.guest_id,
                    "rating": a.rating
                } for a in e.appearances
            ]
        }
        for e in episodes
    ])


@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "guest_id": a.guest_id,
                "rating": a.rating
            } for a in episode.appearances
        ]
    })


@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted successfully")