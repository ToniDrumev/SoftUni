from typing import List
from project.player import Player


class Guild:
	def __init__(self, name: str):
		self.name = name
		self.players:List[Player] = []

	def assign_player(self, player: Player) -> str:
		if player.guild == self.name:
			return f"Player {player.name} is already in the guild."

		if player.guild == "Unaffiliated":
			player.guild = self.name
			self.players.append(player)

			return f"Welcome player {player.name} to the guild {self.name}"

		return  f"Player {player.name} is in another guild."

	def kick_player(self, player_name: str) -> str:
		players = [p for p in self.players if p.name == player_name]

		if not players:
			return f"Player {player_name} is not in the guild."

		player = players[0]

		player.guild = "Unaffiliated"
		self.players.remove(player)

		return f"Player {player_name} has been removed from the guild."

	def guild_info(self) -> str:
		return f"Guild: {self.name}\n" + "\n".join([p.player_info() for p in self.players])
