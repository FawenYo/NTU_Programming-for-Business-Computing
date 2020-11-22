import os


def main():
    solver = "./Pdogs/week7/hw3.py"
    data = "./Pdogs/week7/data.txt"
    os.system("python3 {} < {}".format(solver, data))


if __name__ == "__main__":
    main()
