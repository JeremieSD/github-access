from github import Github

def print_user_info(gAPI):
    print("Name is: " + gAPI.get_user().login)
    print("Full name is: " + gAPI.get_user().name)
    print("Bio is: " + gAPI.get_user().bio)
    print("Location is: "+ gAPI.get_user().location)

def main():
    ans = None
    while (ans != 'y' and ans != 'n'):
      ans = input("Do you want to login?:(y/n)")
    if ans == 'y':
      logged = False
      while(not logged):
        token = input("Enter Github token: ")
        g = Github(token)
        try:
          g.get_user().login
        except:
          print("Authentication denied please try again.")
        else:
          print_user_info(g)
          logged = True
    else:
      g = Github()
      user = g.get_user("torvalds")
      print ("Name is: " + user.login)
      print("Full name is: " + user.name)
      print("Location is: "+ user.location)
      print(f"Public repos: {user.public_repos}")

    

if __name__ == "__main__":
    main()