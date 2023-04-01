import instaloader
import getpass

f = open("followerrs.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()

x = instaloader.Instaloader()
user_name = input("please input your instagram  user name: ")
pass_word = getpass.getpass("please input your password: ") 

x.login(user_name, pass_word)
print("successfuly logged in!")

profile = instaloader.Profile.from_username(x.context, user_name)

new_followers = []
for follower in profile.get_follower():
    new_followers.append(follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "/n")
f.close()