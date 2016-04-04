from app import db

class Post(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    message_id   = db.Column(db.String(50), index=True,unique=True)
    created_time = db.Column(db.DateTime)
    message      = db.Column(db.String(200))
    liked        = db.Column(db.Integer)
    comment = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Message %r>' % (self.message_id)

class Comment(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    comment_id     = db.Column(db.String(30))
    created_time   = db.Column(db.DateTime)
    commenter_name = db.Column(db.String(30))
    commenter_id   = db.Column(db.String(20))
    message        = db.Column(db.String(200))
    liked          = db.Column(db.Integer)
    post_id        = db.Column(db.String(50), db.ForeignKey('post.message_id'))

    def __repr__(self):
        return '<Comment %r>' % (self.comment_id)
