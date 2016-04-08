import urllib2
import json
from apps import db, models

from datetime import datetime


# GLOBAL VARIABLE
#simple data pull App Secret and App ID
APP_ID = "546664045494484"
APP_SECRET = "881d170f5bf1b8c7c396faeb56a22dd9"

#to find go to page's FB page, at the end of URL find username
#e.g. http://facebook.com/walmart, walmart is the username
#list_companies = ["306608096208936","289984354471103"]
list_companies = ["306608096208936"]
graph_url = "https://graph.facebook.com/"
extract_count = 20


def create_post_url(graph_url, extract_count, APP_ID, APP_SECRET): 
	#create authenticated post URL
	post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET + "&limit=" + str(extract_count)
	post_url = graph_url + post_args

	return post_url

def create_comment_url(graph_url, extract_count, post_id, APP_ID, APP_SECRET):
	#create authenticated comment URL
	comment_args = post_id + "/comments/?key=value&access_token=" + APP_ID + "|" \
	               + APP_SECRET + "&limit=" + str(extract_count)
	comment_url = graph_url + comment_args

	return comment_url

def create_likes_url(graph_url, post_id, APP_ID, APP_SECRET):
	#create authenticated like url
	like_args = post_id + "/likes?summary=true&key=value&access_token=" + APP_ID + "|" + APP_SECRET
	like_url = graph_url + like_args

	return like_url
	
def render_to_json(graph_url):
	#render graph url call to JSON
	#print graph_url
	web_response = urllib2.urlopen(graph_url)
	readable_page = web_response.read()
	json_data = json.loads(readable_page)
	
	return json_data
	
def insert_post_database():	
	for company in list_companies:
		#make graph api url with company username
		current_page = graph_url + company
		
		post_url = create_post_url(current_page, extract_count, APP_ID, APP_SECRET)
		json_postdata = render_to_json(post_url)
		json_fbposts = json_postdata["data"]


		#print post messages and ids
		for post in json_fbposts:
			postdb_id      = post["id"]
			postdb_time    = datetime.strptime(post["created_time"], "%Y-%m-%dT%H:%M:%S+0000")
			postdb_message = post["message"]

			# Get like counts
			like_url = create_likes_url(graph_url, post["id"], APP_ID, APP_SECRET)
			json_likedata = render_to_json(like_url)
			postdb_likecount = json_likedata["summary"]["total_count"]
			 
			post = models.Post(message_id=postdb_id,
                    created_time=postdb_time,
                    message=postdb_message,
                    liked=postdb_likecount)

			db.session.add(post)
    	db.session.commit()

def insert_comment_database():
	posts = models.Post.query.all()

	for p in posts:
		post_id = p.message_id
		comment_url = create_comment_url(graph_url, extract_count, post_id, APP_ID, APP_SECRET)
		json_commentdata = render_to_json(comment_url)
		json_fbcomments = json_commentdata['data']

		for comment in json_fbcomments:
			commentdb_id       = comment["id"].split('_')[1]
			commentdb_time     = datetime.strptime(comment["created_time"], "%Y-%m-%dT%H:%M:%S+0000")
			commentdb_person   = comment["from"]["name"]
			commentdb_personid = comment["from"]["id"]
			commentdb_message  = comment["message"]

			like_url = create_likes_url(graph_url, post_id+'_'+commentdb_id, APP_ID, APP_SECRET)
			json_likedata = render_to_json(like_url)
			commentdb_likecount = json_likedata["summary"]["total_count"]

			comment = models.Comment(comment_id=commentdb_id,
                          created_time=commentdb_time,
                          commenter_name=commentdb_person,
                          commenter_id=commentdb_personid,
                          message=commentdb_message,
                          liked=commentdb_likecount,
                          post_id=post_id)

			db.session.add(comment)
		db.session.commit()

def main():
	insert_post_database()
	insert_comment_database()
			
if __name__ == "__main__":
	main()    
