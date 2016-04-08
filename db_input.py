from apps import db, models

from datetime import datetime

str_date = '2016-03-29T15:31:57+0000'
date_object1 = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S+0000')
message1 = '\u7248\u4e3b\u8d34\u6587\uff1a\n\u57fa\u4e8e\u201c\u806a\u660e\u201d\u7684\u4eba\u7c7breport\u4e86\u67d0\u8d34\u6587\uff0c\u5bfc\u81f4\u57fa\u5fb7\u524d\u51e0\u5929\u65e0\u6cd5\u53d1\u5e16\uff0c\u6240\u4ee5\u7d22\u6027\u7ba1\u7406GForms\n\u5728\u6b64\u6211\u4eec\u5e0c\u671b\u5404\u4f4d\u8bfb\u8005\u4eec\u5728\u770b\u7740confession\u7684\u65f6\u5019\uff0c\u5982\u679c\u89c9\u5f97\u6709\u8d34\u6587\u662f\u5728\u8bf4\u4f60\uff0c\u8bf7\u76f4\u63a5pm\u6211\u4eec\uff0c\u4e0d\u8981report\n\u53d1\u5e16\u8005\u4e0d\u4f1a\u6709\u4efb\u4f55\u4e8b\u60c5\uff0c\u800c\u4f60\u53ea\u662f\u5728\u627e\u6211\u4eec\u9ebb\u70e6\n\u8c22\u8c22\n\nAdmin Post:\nDue to \"smart\" people report post, making kid unable to post confessions. We would like to remind readers, if you think the post refers to you, think again why were you being complaint more than just report the post. The confessor will not feel anything, only the admin team will \"dulan\"\nJust pm us and we will remove it if it is really not appropriate \nTQ'

str_date = '2016-03-29T14:27:16+0000'
date_object2 = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S+0000')
message2 = '#K23953\n\u4eca\u5929\u770b\u89c1\u4f60\u7a7fformal\uff0c\u4f60\u90a3\u6e05\u7eaf\u7684\u6837\u5b50\u52a0\u4e0a\u4f60\u767d\u7699\u7684\u808c\u80a4 \u771f\u662f\u53ef\u7231\u6781\u4e86\u3002\n\u5927\u5bb6\u8bf7\u5e2e\u4e2a\u5fd9tag\u5979\u51fa\u6765\uff0c \u4ed6\u4eca\u5929\u7a7f\u767d\u8272\u978b \u9ed1\u8272formal \u518d\u52a0\u4e0a\u7ea2\u8272\u4e66\u5305\u3002\n\u8fd9\u4f4d\u5c0f\u59d0\uff0c\u6211\u771f\u7684\u5f88\u60f3\u8ba4\u8bc6\u4f60\u54e6'


## Create 2 Post object
post1 = models.Post(message_id='306608096208936_497883547081389',
                    created_time=date_object1,
                    message=message1,
                    liked=69)

post2 = models.Post(message_id='306608096208936_497846080418469',
                    created_time=date_object1,
                    message=message2,
                    liked=30)

## Example for Comment
comment1 = models.Comment(comment_id='number in string',
                          created_time=date_object,
                          commenter_name='WayneJunYing',
                          commenter_id='number in string',
                          message='some message',
                          liked=55,
                          post_id='306608096208936_497846080418469')

## Add the object to the database table
db.session.add(post1)
db.session.add(post2)
db.session.add(comment1)
## Finally update the table
db.session.commit()

