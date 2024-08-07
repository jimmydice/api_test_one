"""Module for defining API routes"""

import logging
from flask import Blueprint, request, jsonify
from .models import db, VideoGame
from typing import List, Dict, Union

# Set up logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

api_bp = Blueprint('api', __name__)

@api_bp.route('/videogames', methods=['POST'])
def add_videogame() -> Dict[str, Union[str, int]]:
    """Endpoint to add a new video game to the database.

    :return: Response message and status code
    :rtype: dict
    """
    if request.content_type != 'application/json':
        LOGGER.error(f"Unsupported Media Type: {request.content_type}")
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    
    try:
        new_videogame = VideoGame(
            name=data['name'],
            platform=data['platform'],
            score=data['score']
        )
        db.session.add(new_videogame)
        db.session.commit()
    except KeyError as e:
        LOGGER.error(f"Missing key in request data: {str(e)}")
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    except Exception as e:
        LOGGER.exception("An error occurred while adding the video game")
        return jsonify({"error": "An error occurred while adding the video game"}), 500

    return jsonify({"message": "Video game added successfully!"}), 201

@api_bp.route('/videogames', methods=['GET'])
def get_videogames() -> List[Dict[str, Union[int, str, float]]]:
    """Endpoint to retrieve all video games from the database.

    :return: List of video games
    :rtype: list
    """
    try:
        videogames = VideoGame.query.all()
        videogames_list = [
            {
                "id": vg.id,
                "name": vg.name,
                "platform": vg.platform,
                "score": vg.score
            } for vg in videogames
        ]
    except Exception as e:
        LOGGER.exception("An error occurred while retrieving video games")
        return jsonify({"error": "An error occurred while retrieving video games"}), 500

    return jsonify(videogames_list), 200
