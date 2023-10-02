# Question: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Medium

class Player:
    def __init__(self, player_name, color, starting_score=0):
        self.name  = player_name
        self.color = color
        self.score = starting_score
        
    def get_score(self):
        return self.score
    
    def update_score(self, delta):
        self.score += delta
        
    def set_score(self, score):
        self.score = score
        

class Solution:
    def __init__(self):
        self.players = {}
        
    def initialize_players(self, players, colors):
        for idx in range(len(players)):
            self.players[players[idx]] = Player(players[idx], colors[idx])
            
    def update_scores(self, chain_leader, chain_length):
        if chain_length < 3: return
        for player in self.players.values():
            if player.color == chain_leader:
                player.update_score(chain_length - 2)
        
    def winnerOfGame(self, colors: str) -> bool:
        self.initialize_players(['alice', 'bob'], ['A', 'B'])
        
        if len(colors) == 0: return False
    
        buffer = colors[0]
        buffer_length = 1
        for idx, char in enumerate(colors[1:]):
            if char == buffer:
                buffer_length += 1
                continue
            
            self.update_scores(buffer, buffer_length)
            
            buffer = char
            buffer_length = 1
            
        self.update_scores(buffer, buffer_length)
        return (
            self.players['alice'].get_score() -
            self.players['bob'].get_score()
        ) >= 1
        
                
    # n pieces arranged in a line
    # each piece is colored
    # two types of colors ['A', 'B']
    # colors contain color information of each piece 
    # colors[i] = color of ith piece in n pieces

    # alice and bob are playing a game
    # alice plays first
    # alice can remove a piece colored 'A'
    # if left and right of this piece are also colored 'A'

    # bob can do the same for pieces with colored 'B'

    # alice and bob can't remove pieces from the edge of line
    # if player can't make a move on their turn
    # that player loses 

    # assume alice and bob are making best move at each step
    # return true if alice wins
    # false otherwise

    # if a group of n consecutive pieces have same color
    # a player can make n-2 moves on it

    # alice makes the first move
    # so for alice to win she should be able to make
    # number of moves bob can make + 1
        


# October 02, 2023

'''

# Kunal Wadhwa

'''