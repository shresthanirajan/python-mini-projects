class Team:
    def __init__(self, team_name,):
        self.team_name = team_name
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def show_team(self):
        if not self.characters:
            print("Please add Characters into a Team!")
        else:
            for character in self.characters:
                character.show_info()

    def remove_character(self, character):
        if not self.characters:
            print("No characters in Team! Please Add Characters into a team first.")
            return
        else:
            for characterLoop in self.characters:
                if character.lower() == characterLoop.name.lower():
                    self.characters.remove(characterLoop)
                    print("Successfully Removed!")
                    return
            else:
                print("Nothing Found!")

    def team_attack(self, other_team):
        for character in self.characters:
            if not other_team.characters:
                print("No other Team to attack!")
                return
            else:
                character.attack()
                first_character = other_team.characters[0]
                first_character.take_damage(character.damage)
                if first_character.health <= 0:
                    other_team.characters.remove(first_character)
                    print(f"{first_character.name} has been Defeated!")
                    







