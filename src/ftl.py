from src.Registry import Registry


class FTL:
    def __init__(self, registry: Registry):
        self.id = None
        self.registry = registry

    async def process_command(self, c, m):
        command = m.text.split('.', 1)[1].split(' ', 1)[0]
        await self.registry.execute(command, c, m)

    async def process_listener(self, c, m):
        await self.registry.listen(c, m)
