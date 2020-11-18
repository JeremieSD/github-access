from github import Github

def print_user_info(gAPI):
    print("Name is: " + gAPI.get_user().login)
    print("Full name is: " + gAPI.get_user().name)
    print("Bio is: " + gAPI.get_user().bio)
    print("Location is: "+ gAPI.get_user().location)

def main():
    token = input("Enter Github token: ")
    g = Github(token)
    print_user_info(g)

if __name__ == "__main__":
    main()