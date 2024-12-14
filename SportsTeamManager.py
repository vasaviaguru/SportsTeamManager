class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Position: {self.position}"


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        self.matches = []

    def add_player(self, player):
        self.players.append(player)
        print(f"Player {player.name} added to the team.")

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f"Player {player_name} removed from the team.")
                return
        print(f"Player {player_name} not found in the team.")

    def update_player(self, player_name, new_name=None, new_age=None, new_position=None):
        for player in self.players:
            if player.name == player_name:
                if new_name:
                    player.name = new_name
                if new_age:
                    player.age = new_age
                if new_position:
                    player.position = new_position
                print(f"Player {player_name} updated successfully.")
                return
        print(f"Player {player_name} not found in the team.")

    def view_team(self):
        if not self.players:
            print("No players in the team yet.")
        else:
            print(f"Team: {self.team_name}")
            for player in self.players:
                print(player)

    def schedule_match(self, opponent, date):
        match = {
            "opponent": opponent,
            "date": date
        }
        self.matches.append(match)
        print(f"Match scheduled against {opponent} on {date}.")

    def view_matches(self):
        if not self.matches:
            print("No matches scheduled yet.")
        else:
            print("Scheduled Matches:")
            for match in self.matches:
                print(f"Opponent: {match['opponent']}, Date: {match['date']}")


def main():
    team = Team("CSK")

    while True:
        print("\n1. Add Player\n2. View Team\n3. Remove Player\n4. Update Player\n5. Schedule Match\n6. View Matches\n7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter player's name: ")
            age = int(input("Enter player's age: "))
            position = input("Enter player's position: ")
            player = Player(name, age, position)
            team.add_player(player)

        elif choice == "2":
            team.view_team()

        elif choice == "3":
            name = input("Enter the name of the player to remove: ")
            team.remove_player(name)

        elif choice == "4":
            name = input("Enter the name of the player to update: ")
            new_name = input("Enter new name (leave blank to keep current name): ")
            new_age = input("Enter new age (leave blank to keep current age): ")
            new_position = input("Enter new position (leave blank to keep current position): ")
            new_age = int(new_age) if new_age else None
            team.update_player(name, new_name or None, new_age, new_position or None)

        elif choice == "5":
            opponent = input("Enter opponent team name: ")
            date = input("Enter match date (YYYY-MM-DD): ")
            team.schedule_match(opponent, date)

        elif choice == "6":
            team.view_matches()

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
