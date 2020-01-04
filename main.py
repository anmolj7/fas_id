from fedora.client.fas2 import AccountSystem 
from fedora.client import AuthError
from credentials import USER_NAME, PASSWORD


def get_email(username):
    try:
        fas = AccountSystem(username=USER_NAME, password=PASSWORD)
        people = fas.people_by_key(key='username', search=username, fields=['email'])
        if username in people:
            return people[username]['email']
        return 0 
    except AuthError as e:
        print(str(e))
        print('Edit the credentials in the credentials.py')
        exit()


def main():
    username = input('Enter The username you wanna search: ')
    email = get_email(username)
    if email:
        print(f'User: {username} Email -> {email}')
    else:
        print('The given user doesn\'t exist')


if __name__ == "__main__":
    main()