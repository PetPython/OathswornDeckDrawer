from src.decks.deck_builder import DeckBuilder
from src.decks.deck_color import DeckColor
from src.decks.deck_controller import DeckController
from src.decks.deck_type import DeckType


class DeckControllerInitializer:
    @staticmethod
    def initialize() -> DeckController:
        player_white_deck = DeckBuilder.form_initial_deck(DeckType.Player, DeckColor.White)
        enemy_white_deck = DeckBuilder.form_initial_deck(DeckType.Enemy, DeckColor.White)
        player_yellow_deck = DeckBuilder.form_initial_deck(DeckType.Player, DeckColor.Yellow)
        enemy_yellow_deck = DeckBuilder.form_initial_deck(DeckType.Enemy, DeckColor.Yellow)
        player_red_deck = DeckBuilder.form_initial_deck(DeckType.Player, DeckColor.Red)
        enemy_red_deck = DeckBuilder.form_initial_deck(DeckType.Enemy, DeckColor.Red)
        player_black_deck = DeckBuilder.form_initial_deck(DeckType.Player, DeckColor.Black)
        enemy_black_deck = DeckBuilder.form_initial_deck(DeckType.Enemy, DeckColor.Black)

        return DeckController([
            player_white_deck, enemy_white_deck,
            player_yellow_deck, enemy_yellow_deck,
            player_red_deck, enemy_red_deck,
            player_black_deck, enemy_black_deck,
        ])
