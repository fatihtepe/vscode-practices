from decouple import config


userID = 'tepe'
password = 'thepassword'

print(userID, password)

'''Whenever you upload your project or code on your 
GitHub containing some secret keys and passwords, and 
if that repo is public, remember that the users running 
the file will have at least read access to it and can 
easily grab the passwords. Always think about security 
very carefully, it’s important. E.g., you have to always hide 
your secret keys in a Django application, google OAuth credential 
keys or tokens, etc.
    I will straightforwardly guide you. After this tutorial, 
you will be able to hide your passwords from anyone who opens 
your project on github.
    We will make a sample python file let’s say temp.py, and try 
hiding the password in it.
'''
userID = 'tepe'
password = 'thepassword'

print(userID, password)

'''Take this code, for example; if I upload this code on Github, 
obviously, I don't want other people to see the password 
contained in my .py file.
I will need the config function found in the ‘decouple’ 
module in python to hide the password. To install this module, 
run the following command on your terminal:'''

pip install python-decouple

'''After this gets installed, make a .env file in the same folder 
as our test.py file, and copy-paste the userID and password 
in that file, like this,'''

userID = 'tepe'
password = 'thepassword'

'''Note: This method will only work by making a .env file; 
no other file format will work.
Getting back to our test.py file, make changes like in the code below,'''

from decouple import config


userID = 'tepe'
password = 'thepassword'

print(userID, password)

'''You can guess how this will work. The userID and password 
will be extracted from the .env file. The default argument 
in the config function is there because in case the given 
field(first argument) is not in the .env file, 
it should not throw an error and initialize the value of that 
field as an empty string or any other value, just put it in 
quotes in default.
    The problem of anyone opening our repo and seeing the 
password remains because he/she can open the .env file and see the
password. To prevent that, make a .gitignore file in the 
same folder as .env and test.py,and add .env in 
the .gitignore file, like this.'''
.env
'''This .env file will be ignored by Github and won't be visible 
on our repo. So our userID and password are safe and secure now.
If you want other users to use your scripts, write the 
documentation and save that in a Readme.md with details about 
making a .env file and running the code, and uploading it to 
your GitHub repo. Other users can use your script by entering 
their own password and userID in their self-made .env file.
Signing off
Using the same method, you can hide secret keys in your Django 
project, google OAuth tokens, and other secret info and 
passwords. That’s all for this blog. In case of any query, 
you can comment on this blog or mail me.
Thanks and Happy Learning!'''
'''source ==> https://medium.com/analytics-vidhya/hiding-secret-keys-and-passwords-in-python-2950c6a4359'''
