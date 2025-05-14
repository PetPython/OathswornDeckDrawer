import random

from src.card import Card
from src.decks.deck import Deck
from src.decks.deck_color import DeckColor
from src.decks.deck_type import DeckType


class DeckController:
    def __init__(self, decks: list[Deck]):
        self.decks = decks
        self._shuffle_all_decks()

    def get_target_deck(self, deck_type: DeckType, deck_color: DeckColor) -> Deck:
        return next(deck for deck in self.decks if deck.type == deck_type and deck.color == deck_color)

    @staticmethod
    def get_discard_pile(deck: Deck) -> list[Card]:
        return deck.discard_pile

    @staticmethod
    def get_number_of_misses_in_discard_pile(deck: Deck) -> int:
        return deck.discard_pile.count(Card.Miss)

    @staticmethod
    def get_number_of_misses_in_draw_pile(deck: Deck) -> int:
        return deck.draw_pile.count(Card.Miss)

    def draw_cards(self, decks_and_cards: list[tuple[Deck, int]]) -> list[tuple[Deck, list[Card]]]:
        cards = []

        for deck, card_count in decks_and_cards:
            drawn_cards = self._draw_cards_from_one_deck(deck, card_count)
            cards.append((deck, drawn_cards))

        return cards

    def renew_draw_pile(self, deck: Deck):
        deck.draw_pile.extend(deck.discard_pile)
        self._shuffle_draw_pile(deck)
        deck.discard_pile.clear()

    def _shuffle_all_decks(self) -> None:
        for deck in self.decks:
            self._shuffle_draw_pile(deck)

    def _draw_cards_from_one_deck(self, deck: Deck, card_count: int) -> list[Card]:
        cards_to_draw = []

        for _ in range(card_count):
            card = self._move_first_card_from_draw_pile_to_discard_pile(deck)
            self._check_and_renew_draw_pile(deck)
            cards_to_draw.append(card)

        print(
            f"Drawn {len(cards_to_draw)} cards from {deck.type} {deck.color} deck: "
            f"{[card.name for card in cards_to_draw]}. "
            f"{len(deck.draw_pile)} cards left, with {self.get_number_of_misses_in_draw_pile(deck)} misses among them."
        )

        return cards_to_draw

    @staticmethod
    def _shuffle_draw_pile(deck: Deck) -> None:
        print(f"Shuffling {deck.type} {deck.color} deck")
        random.shuffle(deck.draw_pile)

    def _check_and_renew_draw_pile(self, deck: Deck) -> None:
        if len(deck.draw_pile) == 0:
            print(f"{deck.type} {deck.color} deck is out of cards in draw pile")
            self.renew_draw_pile(deck)

    @staticmethod
    def _move_first_card_from_draw_pile_to_discard_pile(deck: Deck) -> Card:
        card = deck.draw_pile.pop(0)
        deck.discard_pile.append(card)
        return card
