import json

from src.card import Card
from src.constants import DECK_DATA_FILE
from src.decks.deck import Deck
from src.decks.deck_color import DeckColor
from src.decks.deck_type import DeckType


class DeckBuilder:
    @staticmethod
    def form_initial_deck(deck_type: DeckType, deck_color: DeckColor) -> Deck:
        cards = []

        with open(DECK_DATA_FILE) as file:
            all_deck_data = json.load(file)
            target_deck_data = all_deck_data.get(deck_color)

            for data in target_deck_data:
                for card_type, card_count in data.items():
                    cards.extend([Card[card_type]] * card_count)

        return Deck(deck_type=deck_type, deck_color=deck_color, cards=cards)
