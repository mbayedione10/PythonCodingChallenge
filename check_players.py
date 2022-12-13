def check(n, m, games):
    # Create a set to store all pairs of players that have played against each other
    played_together = set()

    # Loop through the games and add each pair of players to the set
    for game in games:
        # Split the game into two teams
        team_1 = game[:n//2]
        team_2 = game[n//2:]

        # Loop through the players on each team and add each pair to the set
        for player_1 in team_1:
            for player_2 in team_2:
                played_together.add((player_1, player_2))

    # Loop through all possible pairs of players such that 1 < x < y < n
    for x in range(1, n+1):
        for y in range(x+1, n+1):
            # If x and y haven't played against each other, return False
            if (x, y) not in played_together:
                return False

    # If all pairs of players have played against each other, return True
    return True


if __name__ == '__main__':
    print(check(2, 1, [[1, 2]]))
    print(check(4, 2, [[1, 2, 3, 4], [4, 3, 1, 2]]))
    print(check(4, 2, [[1, 2, 3, 4], [1, 3, 2, 4]]))

    print(check(6, 6, [[1, 6, 3, 4, 5, 2], [6, 4, 2, 3, 1, 5], [4, 2, 1, 5, 6, 3], [
        4, 5, 1, 6, 2, 3], [3, 2, 5, 1, 6, 4], [2, 3, 6, 4, 1, 5]]))

    print(check(6, 6, [[3, 1, 4, 5, 6, 2], [5, 3, 2, 4, 1, 6], [5, 3, 6, 4, 2, 1], [
        6, 5, 3, 2, 1, 4], [5, 4, 1, 2, 6, 3], [4, 1, 6, 2, 5, 3]]))
