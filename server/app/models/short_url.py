from app.extensions import db

class ShortUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(20), unique=True, nullable=False)
    clicks = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
