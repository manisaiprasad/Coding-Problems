def tournamentWinner(competitions, results):
    # Write your code here.
	teams = {}
	for idx in range(len(competitions)):

		team1 = competitions[idx][0]
		team2 = competitions[idx][1]

		if results[idx] == 0:
			if team2 in teams:
				teams[team2] = teams[team2] + 3
			else:
				teams[team2] = 3

		if results[idx] == 1:
			if team1 in teams:
				teams[team1] = teams[team1] + 3
			else:
				teams[team1] = 3

	max_key = max(teams, key=teams.get)
    return max_key
