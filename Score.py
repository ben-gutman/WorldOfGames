def add_score(difficulty):
    points_of_winning = (difficulty*3)+5
    try:
        f = open("Scores.txt", "r+")
        current_score = int(f.read())
        new_score = current_score+points_of_winning
        f.seek(0)
        f.write(str(new_score))
    except FileExistsError:
        print(f"File already exist")
    except:
        print("unexpected error")
    finally:
        f.close()
