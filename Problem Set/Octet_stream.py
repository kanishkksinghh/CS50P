def main():
    filename = input("File Name:").strip().lower()

    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith(".jpg"):
        print("image/jpg")
    elif filename.endswith(".jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith(".pdf"):
        print("application/pdf")
    elif filename.endswith(".txt"):
        print("txt/plain")
    elif filename.endswith(".zip"):
        print("application/plain")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()



