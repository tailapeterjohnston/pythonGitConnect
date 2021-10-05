user_password = str(input("Whats your password?: "))


def main():
    make_astrisks(user_password)


def make_astrisks(user_password):
    for i in range(0, len(user_password)):
        print("*", end="")

def check_spaces(user_password):
    for i in range(0, len(user_password)):
        user_password
