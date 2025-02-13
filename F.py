def check_size(num):
    return len(str(num)) == len(str(num * 2))

def main():
    num = int(input("Enter a number: "))
    print("Same size" if check_size(num) else "Different size")

if __name__ == "__main__":
    main()
