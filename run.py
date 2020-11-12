import os


def main():
    solver = "./Pdogs/week6/hw3.py"
    data = "./Pdogs/week6/data.txt"
    os.system("python3 {} < {}".format(solver, data))


if __name__ == "__main__":
    main()
