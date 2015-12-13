## SSL Chat


### About
* Nothing too fancy, just a python SSL chat client/server program. I wrote this because I frequently needed a
template for how to do python raw SSL sockets.
* The initial version of this program just stands up an SSL wrapped socket for chat. The next stage will derive a
random symmetric AES encryption key, exchange said key, and then encrypt all messages going forward with said
symmetric key.  This all seems like heavy lifting, but the goal is that the program will be