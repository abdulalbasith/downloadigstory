import instaloader

loader = instaloader.Instaloader()
user=input ("What is your username? ")
loader.interactive_login(user)
target = input ("Who is your target? ")


loader.download_storyitem(item,':stories')
    

