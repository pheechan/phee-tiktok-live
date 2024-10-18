import json
import pygame
from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, GiftEvent
from Territorywar_game import Player, is_valid_move

def load_user_country_mapping():
    try:
        with open("user_country_mapping.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_country_mapping(mapping):
    with open("user_country_mapping.json", "w") as file:
        json.dump(mapping, file)

def main():
    # Initialize the TikTok Live client with your username
    client = TikTokLiveClient(unique_id="your_tiktok_username")

    # Create a list of players (countries)
    players = {
        "th": Player((0, 255, 0), (0, 0)),  # Thailand
        "jp": Player((255, 0, 0), (1, 0)),  # Japan
        "kr": Player((0, 0, 255), (2, 0)),  # South Korea
        "us": Player((255, 255, 0), (3, 0))  # United States
    }

    user_country_mapping = load_user_country_mapping()

    # Define what happens when a comment is received
    @client.on("comment")
    async def on_comment(event: CommentEvent):
        country_name = event.comment.lower()
        if country_name in players:
            user_country_mapping[event.user.uniqueId] = country_name
            save_user_country_mapping(user_country_mapping)
            players[country_name].gain_territory(1)
            print(f"{event.user.nickname} increased {country_name}'s territory by 1 pixel.")

    # Define what happens when a gift is sent
    @client.on("gift")
    async def on_gift(event: GiftEvent):
        user_id = event.user.uniqueId
        if user_id in user_country_mapping:
            country_name = user_country_mapping[user_id]
            boost_amount = event.gift.repeat_count  # Boost amount based on the number of gifts
            players[country_name].gain_territory(boost_amount)
            print(f"{event.user.nickname} boosted {country_name}'s territory by {boost_amount} pixels with a gift.")

    # Initialize pygame
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    GRID_SIZE = 20
    FPS = 30
    BACKGROUND_COLOR = (0, 0, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Territory War")
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        for player in players.values():
            player.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    client.run()

if __name__ == "__main__":
    main()