import json

def get_winner(choice1, choice2):
    # כללי המשחק: מי מנצח
    if choice1 == choice2:
        return None  # תיקו, אין מנצח
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        return 1  # השחקן הראשון מנצח
    else:
        return 2  # השחקן השני מנצח
        
def game(results_filename):
   try:     with open("results_filename", "r") as file:            
   except FileNotFoundError:     
       print("The file was not found.")
   except IOError:     
       print("An error occurred while trying to open the file.")
         for line in file:
            data = line.strip().split()  # מפצל את השורה לרשימה של מילים
            if len(data) == 4:
                player1, choise1, player2, choise2 = data  # מתעלמים מהבחירות ושומרים רק את השמות
                      winner = get_winner(choice1, choice2)

                # עדכון הניקוד במילון בהתאם לתוצאה
                if winner == 1:
                    if player1 in players_dict:
                        players_dict[player1] += 1
                    else:
                        players_dict[player1] = 1
                    if player2 not in players_dict:
                        players_dict[player2] = 0
                elif winner == 2:
                    if player2 in players_dict:
                        players_dict[player2] += 1
                    else:
                        players_dict[player2] = 1
                    if player1 not in players_dict:
                        players_dict[player1] = 0
                else:
                    # במקרה של תיקו, נוודא שהשחקנים קיימים עם ערך התחלתי אם לא היו במילון
                    if player1 not in players_dict:
                        players_dict[player1] = 0
                    if player2 not in players_dict:
                        players_dict[player2] = 0

    
    # todo: implement this function
    print(f'starting the game with {results_filename}')

    # todo: due to possible difference in file encodings between operating systems, you may need to add
    #  utf8 encoding type when opening a file, as an example: with open(<file name>, 'r', encoding='utf8') as fin
    #  python developers plan to make utf8 a default at 3.15 - https://peps.python.org/pep-0686/


    winner = ''  # todo: assign player name or "tie"
    return winner


# todo: fill in your student ids
students = {'id1': '207748518', 'id2': '209342278'}

if __name__ == '__main__':
    with open('config-rps.json', 'r') as json_file:
        config = json.load(json_file)

    winner = game(config['results_filename'])
    print(f'the winner is: {winner}')
