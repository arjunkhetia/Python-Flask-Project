from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def login():
    data = { 'message': "User successful!" }
    return jsonify(data), 200
