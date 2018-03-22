import os


if __name__ == '__main__':
    txtFiles = os.listdir("../data")
    for file in txtFiles:
        for x in range(10):
            print(file)