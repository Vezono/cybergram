from src import BaseCommand

class StartBotguiCommand(BaseCommand):
    text = "startbot"

    async def execute(self, c, m):
        print('hi!')

commands = [StartBotguiCommand]
listeners = []