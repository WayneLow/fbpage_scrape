from flask import render_template
from app import app, db
from .models import Post

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'UTAR Confession'}
    posts = Post.query.all()
    post_array = []
    for post in posts:
      message_id = post.message_id
      page_post = message_id.split('_',1)
      url='https://www.facebook.com/'+page_post[0]+'/posts/'+page_post[1]
      post_array.append({'url':url})    
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=post_array)
