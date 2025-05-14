from src.card import Card
from src.decks.deck_color import DeckColor
from src.decks.deck_type import DeckType


class Deck:
    def __init__(self, deck_type: DeckType, deck_color: DeckColor, cards: list[Card]):
        self.type = deck_type
        self.color = deck_color
        self.draw_pile = cards
        self.discard_pile: list[Card] = []
