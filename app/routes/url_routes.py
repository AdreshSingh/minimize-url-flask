from flask import Blueprint, abort, redirect, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.short_url import ShortUrl
import uuid

url_bp = Blueprint("url", __name__)

@url_bp.route("/shorten", methods=["POST"])
@jwt_required()
def shorten_url():
    user_id = get_jwt_identity()
    data = request.json

    short_code = str(uuid.uuid4())[:6]

    short_url = ShortUrl(
        original_url=data["original_url"],
        short_code=short_code,
        user_id=user_id
    )

    db.session.add(short_url)
    db.session.commit()

    return jsonify({
        "short_url": f"http://localhost:5000/url/{short_code}"
    })


@url_bp.route("/<string:short_code>", methods=["GET"])
def redirect_short_url(short_code):
    url = ShortUrl.query.filter_by(short_code=short_code).first()

    if not url:
        abort(404, description="Short URL not found")

    # Optional: track clicks
    url.clicks += 1
    db.session.commit()

    return redirect(url.original_url, code=302)