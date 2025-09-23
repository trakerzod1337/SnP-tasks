class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError('WrongNumberOfPlayersError')

    valid_moves = ['R', 'S', 'P']
    for player in players:
        if player[1] not in valid_moves:
            raise NoSuchStrategyError('NoSuchStrategyError')

    player1, move1 = players[0]
    player2, move2 = players[1]

    if move1 == move2:
        return f'{player1} {move1}'
    elif (move1 == 'R' and move2 == 'S') or (move1 =='S' and move2 == 'P') or (move1 == 'P' and move2 == 'R'):
        return f'{player1} {move1}'
    else:
        return f'{player2} {move2}'


#Тестирование
try:
    result = rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
    print(result)
except WrongNumberOfPlayersError:
    print("WrongNumberOfPlayersError")


try:
    result = rps_game_winner([['player1', 'P'], ['player2', 'A']])
    print(result)
except NoSuchStrategyError:
    print("NoSuchStrategyError")


try:
    result = rps_game_winner([['player1', 'P'], ['player2', 'S']])
    print(result)
except Exception as e:
    print(e)


try:
    result = rps_game_winner([['player1', 'P'], ['player2', 'P']])
    print(result)
except Exception as e:
    print(e)