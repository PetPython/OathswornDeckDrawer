from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.gui.deck_screen import DeckScreen
from src.gui.main_screen import MainScreen


class OathswornApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))

        player_screen = DeckScreen(name='player', title="Player")
        enemy_screen = DeckScreen(name='enemy', title="Enemy")

        sm.add_widget(player_screen)
        sm.add_widget(enemy_screen)
        return sm
