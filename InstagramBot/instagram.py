from instagrapi import Client
import getpass
import os

# Create a client
cl = Client()

# Login with input
username = input("Enter your Instagram username/email/phone: ")
password = getpass.getpass("Enter your Instagram password: ")

try:
    cl.login(username, password)
    print("Logged in successfully!")
except Exception as e:
    print(f"Login failed: {e}")
    exit()

# Menu loop
def menu():
    while True:
        print("\nChoose an action:")
        print("1. Follow a user")
        print("2. Post a photo with caption")
        print("3. Post a story")
        print("4. Delete a post")
        print("5. Remove a follower")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_to_follow = input("Enter username to follow: ")
            user_id = cl.user_id_from_username(user_to_follow)
            cl.user_follow(user_id)
            print(f"Followed {user_to_follow}")

        elif choice == "2":
            image_path = input("Enter full image path: ")
            caption = input("Enter caption: ")
            cl.photo_upload(image_path, caption)
            print("Photo posted")

        elif choice == "3":
            image_path = input("Enter full image path for story: ")
            cl.photo_upload_to_story(image_path)
            print("Story posted")

        elif choice == "4":
            media_id = input("Enter Media ID of the post to delete: ")
            cl.media_delete(int(media_id))
            print("Post deleted")

        elif choice == "5":
            username_to_remove = input("Enter username to remove from followers: ")
            user_id = cl.user_id_from_username(username_to_remove)
            cl.user_remove_follower(user_id)
            print(f"Removed {username_to_remove} from followers")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")

menu()
