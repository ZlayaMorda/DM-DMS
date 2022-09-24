## Mininmal requirements:
* User's role:
  * default
  * moderatore
  * admin
---
* Default user:
  * authentification
  * create, redact and del a page
  * add and del the tags in a page
  * subscribe a page
  * write, del the posts
  * add the emotions as a reaction
---
* Moderatore:
  * ban any page for the time
  * del any posts
---
* Admin:
  * as the moderatore + ban any user

---
DB scheme:

![alt text](pictures/diagram.png)

---
DB description:

__Highlighted__ fields are primary keys or part of them

* User
all users, who may use app
  * __IdUser__ - uuid (universal unical identifier)
  * Name - text (an user name of the variable length)
  * LastName - text (an user lastname of the variable length)
  * Email - text (an user email of the variable length)
  * Password - text (an user password of the variable length)
  * Image_s3_path - text (an user avatar image path of the  variable length)
  * Role - text (an user role of the variable length, cases: user, moderatore, admin)
  * Is_blocked - bool (is user banned or not)
  
* Log
logs for user actions
  * __IdUser__ - uuid (foriegn key)
  * DateTime - time (time of action)
  * Action - text (an user action for log)
  
* Chat
chat for communication with users
  * __IdChat__ - uuid
  * Name - text (a chat name)
  * Admin - uuid (IdUser, one to one chat admin)
  
* ChatUser
many to many table
  * __IdChat__ - uuid (foriegn key)
  * __IdUser__ - uuid (foriegn key)
  
* Message
user message in a chat
  * __IdChat__ - uuid (foriegn key)
  * __IdUser__ - uuid (foriegn key)
  * content - text (message content)
  * DataTime - time (message sending time)
  
* Page
User's page with own posts and tags
  * __IdPage__ - uuid
  * Name - text (page name)
  * Description - text (description of the page)
  * IdOwner - uuid (foriegn key)
  * UnblockDate - time (when would be unbanned)
  
* Followers
many to many table betweeb users and pages
  * __IdPage__ - uuid (foriegn key)
  * __IdUser__ - uuid (foriegn key)
  
* Tag
tag to find and group pages
  * __Name__ - text (tag name)
  
* PageTag
many to many table
  * __IdPage__ - uuid (foriegn key)
  * __Name__ - text (foriegn key, tag name)
  
* Post
content of the page, may reply other posts
  * __IdPost__ - uuid
  * IdPage - uuid (foriegn key)
  * IdUser - uuid (foriegn key)
  * Content - text (post content)
  * ReplyPostId - uuid (foreign key for reply post)
  * CreatedAt - time (when created)
  * UpdatedAt - time (when updated)
  
* Reaction
reaction for the post, user may set some different for posts
  * __IdPost__ - uuid (foreign key)
  * __IdUser__ - uuid (foreign key)
  * Likes - bool
  * Dislikes - bool
  ..
---
Completed and normalized DB:

![alt text](pictures/norm_3.png)
