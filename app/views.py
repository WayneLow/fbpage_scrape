from flask import render_template
from app import app, db
from .models import Post, Comment

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'UTAR Confession'}
    #posts = Post.query.all()
    posts = Post.query.order_by('liked desc').all()
    post_array = []

    for post in posts:
      comment_list = []

      message_id = post.message_id
      page_post = message_id.split('_',1)
      url='https://www.facebook.com/'+page_post[0]+'/posts/'+page_post[1]
      #comments = Comment.query.filter_by(post_id=message_id).order_by('created_time asc')
      comments = Comment.query.filter_by(post_id=message_id)
      for comment in comments:
        comment_list.append([comment.commenter_name,
                             comment.message,
                             comment.liked])

      post_array.append({'url':url,'comments':comment_list})
   
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=post_array)
