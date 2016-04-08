from apps import db, models

posts = models.Post.query.all()
print posts

for p in posts:
    db.session.delete(p)


db.session.commit()
