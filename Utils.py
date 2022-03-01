def create_new_file():
    try:
        f = open("Scores.txt", "w+")
        f.write("0")
    except FileExistsError:
        print(f"File allready exist")
    except:
        print("unexpected error")
    finally:
        f.close()
