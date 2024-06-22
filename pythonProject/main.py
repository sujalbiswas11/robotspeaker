import os
if __name__ == '__main__':
    print("welcome to dynamospeaker 1.1 created by sujal")
    while True:
        x = input("enter what you want me to speak:")
        if x== "quit":
            os.system(f"say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)



