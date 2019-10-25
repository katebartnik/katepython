from random import randint


class Game:
    def __init__(self):
        self.player_score_index = 'score'

        self.players = {
            'human': {
                'score': 0
            },
            'ai': {
                'score': 0
            }
        }

        self.available_tools_to_select = {
            0: "Paper",
            1: "Scissors",
            2: "Rock",
        }

    def resolve_winner_index(self, player_option):
        ai_option = self.generate_random_tool_pick()

        if (player_option == 0 and ai_option == 1) or (player_option == 2 and ai_option == 0) or (player_option == 1 and ai_option == 2):
            return 'ai'
        elif (player_option == 1 and ai_option == 0) or (player_option == 0 and ai_option == 2) or (player_option == 2 and ai_option == 1):
            return 'human'
        elif ai_option == player_option:
            return 'draw'

    def count_points(self, winner_index):
        self.players[winner_index][self.player_score_index] += 1

    def generate_random_tool_pick(self):
        return randint(0, len(self.available_tools_to_select) - 1)

    def print_score(self):
        print("Player: " + player_index + ", score: " + str(self.players[player_index][self.player_score_index]))
        for player_index in self.players:
            pass

    def print_options(self):
        for tool_index in self.available_tools_to_select:
            print("[" + str(tool_index) + "] " + self.available_tools_to_select[tool_index])


game_object = Game()

print("Witamy w dojebanej grze w kamień papier nożyce!")
print()

while True:
    print("Wybierz swoje niecne narzędzie: ")
    game_object.print_options()
    tool_index = int(input(" "))
    winner_index = game_object.resolve_winner_index(tool_index)

    if winner_index != 'draw':
        game_object.count_points(winner_index)
    else:
        print('Remis!')

    game_object.print_score()

    play_more = input("Czy grasz dalej, Y/n? ")
    if "n" == play_more:
        break
