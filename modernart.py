import random

# Constants for game setup
NUMBER_OF_ROUNDS = 4
ARTISTS_INFO = {
    'Krypto': 15,
    'Yoko': 15,
    'Christin P.': 15,
    'Karl Gitter': 13,
    'Lite Metal': 12
}

# Constants representing different types of auctions
OPEN_AUCTION = 'Open Auction'
SEALED_AUCTION = 'Sealed Auction'
FIXED_PRICE = 'Fixed Price'
DOUBLE_AUCTION = 'Double Auction'

# Artwork class
class Artwork:
    def __init__(self, artist, auction_type):
        self.artist = artist
        self.auction_type = auction_type

    def __repr__(self):
        return f"Artwork by {self.artist.name}, Auction Type: {self.auction_type}"

# Artist class
class Artist:
    def __init__(self, name):
        self.name = name
        self.popularity = 0  # This can be a measure of how often their art has been sold

# Auction class
class Auction:
    def __init__(self, artwork):
        self.artwork = artwork
        self.bids = []

    def place_bid(self, player, amount):
        self.bids.append((player, amount))

    def resolve_auction(self):
        # This function would handle different auction types differently
        # For now, let's assume it's an open auction where the highest bid wins
        return max(self.bids, key=lambda x: x[1], default=(None, 0))

# Player class
class Player:
    def __init__(self, strategy):
        self.money = 100  # Starting money, could be any value relevant to the game
        self.artworks = []
        self.strategy = strategy

    def take_turn(self):
        # Placeholder for player taking a turn, which could involve initiating an auction
        pass

    def bid(self, auction):
        # Placeholder for player bid logic, which would be based on their strategy
        bid_amount = self.strategy.determine_bid(auction.artwork, self.money)
        auction.place_bid(self, bid_amount)
    
    def __repr__(self):
        # This method is used to print a readable string representation of the player
        return f"Player({self.strategy}, Money: {self.money}, Artworks: {[artwork.artist for artwork in self.artworks]})"


# Strategy class (to be implemented for different bots)
class Strategy:
    def determine_bid(self, artwork, money):
        # Simple example strategy, always bids a flat rate
        return min(money, 10)  # Never bid more than you have, or more than 10

# Game class
class Game:
    def __init__(self, num_players):
        self.players = [Player(f'Player {i+1}') for i in range(num_players)]
        self.artists = [Artist(name) for name in ARTISTS_NAMES]
        self.deck = self.create_deck()
        self.round = 1

    def play_round(self):
        # Simulate a round of the game
        for player in self.players:
            player.take_turn()
        # At the end of the round, print the game state
        self.print_game_state()
    
    def print_game_state(self):
        print(f"Game State at the end of round {self.round}:")
        for player in self.players:
            print(player)
        print()  # Just for a cleaner output


    def play_game(self):
        # Play through the entire game
        while not self.is_game_over():
            self.play_round()
            self.round += 1
        self.declare_winner()

    def is_game_over(self):
        # Check if the game should end
        return self.round > 4  # Example condition, typically when all rounds are done

    def declare_winner(self):
        # Determine and declare the winner of the game
        richest_player = max(self.players, key=lambda p: p.money)
        print(f"The winner is {richest_player} with ${richest_player.money}")

# Example of creating a game with players and a simple strategy
def main():
    strategies = [Strategy() for _ in range(4)]  # Assuming 4 players
    players = [Player(strategy) for strategy in strategies]
    game = Game(players)
    game.play_game()

if __name__ == "__main__":
    main()
