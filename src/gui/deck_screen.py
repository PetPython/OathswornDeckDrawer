from kivy.properties import StringProperty, DictProperty
from kivy.uix.screenmanager import Screen

from src.decks.deck_color import DeckColor
from src.decks.deck_type import DeckType
from src.helpers.deck_controller_initializer import DeckControllerInitializer


class DeckScreen(Screen):
    title = StringProperty("")
    decks_click_count = DictProperty({
        "White": 0,
        "Yellow": 0,
        "Red": 0,
        "Black": 0,
    })
    decks_remaining_cards = DictProperty({
        "White": 18,
        "Yellow": 18,
        "Red": 18,
        "Black": 18,
    })
    decks_remaining_misses = DictProperty({
        "White": 6,
        "Yellow": 6,
        "Red": 6,
        "Black": 6,
    })
    draw_result = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.deck_controller = DeckControllerInitializer.initialize()

    def on_back_button_press(self):
        self._reset_deck_screen()
        self.manager.current = "main"

    def on_deck_button_release(self, deck_color_str: str):
        match DeckColor[deck_color_str]:
            case DeckColor.White:
                self.decks_click_count["White"] += 1
            case DeckColor.Yellow:
                self.decks_click_count["Yellow"] += 1
            case DeckColor.Red:
                self.decks_click_count["Red"] += 1
            case DeckColor.Black:
                self.decks_click_count["Black"] += 1

    def on_shuffle_button_release(self, deck_color_str: str):
        deck = self.deck_controller.get_target_deck(DeckType[self.title], DeckColor[deck_color_str])
        self.deck_controller.renew_draw_pile(deck)
        self._reset_deck_remaining_cards(deck_color_str)
        self._reset_deck_remaining_misses(deck_color_str)

    def on_draw_button_release(self):
        self.draw_result = ""

        deck_and_cards = []

        for deck_color_str, click_count in self.decks_click_count.items():
            deck = self.deck_controller.get_target_deck(DeckType[self.title], DeckColor[deck_color_str])
            deck_and_cards.append((deck, click_count))

        drawn_cards = self.deck_controller.draw_cards(deck_and_cards)

        for deck, cards in drawn_cards:
            if cards:
                self.draw_result += f"{deck.color}: {" ".join(cards)}, "

        self.draw_result = self.draw_result[:-2]

        self.set_decks_remaining_cards()
        self.set_decks_remaining_misses()
        self._reset_decks_click_count()

    def on_continue_button_release(self):
        deck_and_cards = []

        for deck_color_str, click_count in self.decks_click_count.items():
            deck = self.deck_controller.get_target_deck(DeckType[self.title], DeckColor[deck_color_str])
            deck_and_cards.append((deck, click_count))

        drawn_cards = self.deck_controller.draw_cards(deck_and_cards)

        self.draw_result += "\n"
        for deck, cards in drawn_cards:
            if cards:
                self.draw_result += f"{deck.color}: {" ".join(cards)}, "

        self.draw_result = self.draw_result[:-2]

        self.set_decks_remaining_cards()
        self.set_decks_remaining_misses()
        self._reset_decks_click_count()

    def set_decks_remaining_cards(self):
        for color in DeckColor:
            deck = self.deck_controller.get_target_deck(DeckType[self.title], DeckColor[color])
            self.decks_remaining_cards[color] = len(deck.draw_pile)

    def set_decks_remaining_misses(self):
        for color in DeckColor:
            deck = self.deck_controller.get_target_deck(DeckType[self.title], DeckColor[color])
            self.decks_remaining_misses[color] = self.deck_controller.get_number_of_misses_in_draw_pile(deck)

    def _reset_deck_screen(self):
        self._reset_decks_click_count()
        self.ids.continue_btn.disabled = True

    def _reset_decks_click_count(self):
        self.decks_click_count["White"] = 0
        self.decks_click_count["Yellow"] = 0
        self.decks_click_count["Red"] = 0
        self.decks_click_count["Black"] = 0

    def _reset_deck_remaining_cards(self, deck_color_str: str):
        self.decks_remaining_cards[deck_color_str] = 18

    def _reset_deck_remaining_misses(self, deck_color_str: str):
        self.decks_remaining_misses[deck_color_str] = 6
