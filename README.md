# cybergram v0.4.0-beta
## Authors
Made by *vezono* and *Teacater*

## Configuration
First, you need to create `accounts.toml`, which contains api_id and api_hash, list of accounts and their settings.
```toml
# accounts.toml
[config]
api_id = 1234
api_hash = "abcabcabcabc"

[user1]
name = "user1"

[user2]
name = "user2"
enabled = ["example", "sugar"] # only "example" and "sugar" modules will be used by this user

[user3]
name = "user3"
disabled = ["apple"] # all modules except "apple" module will be used
api_id = 4444 
api_hash = "eeeeeeeeeee"  # overlaps data in config section
```

## Module creation
Modules are stored in `modules` directory.
**Module** can either be single file (`module.py`) or a package (`module/__init__.py`).
A module consists of **commands** and **listeners**. While commands only used for responding to your commands, listeners can react to any event.

### Command example:
```python
from src import BaseCommand

class ExampleCommand(BaseCommand):
    def __init__(self):
        super().__init__('example') # bot will respond to ".example" command

    async def execute(self, c: pyrogram.Client, m: pyrogram.types.Message):
        await m.reply('This is an example command!')
```

### Listener example:
```python
from src import BaseListener

class ExampleListener(BaseListener):
    async def execute(self, c: pyrogram.Client, m: pyrogram.types.Message):
        # here you should provide some if's and else's
        await m.reply('I can hear you!')

```

At the and of the main file of the module, you must provide the list of your commands and listeners for core to import them.
```java
commands = [ExampleCommand]
listeners = [ExampleListener]
```


## Advanced Features
### `src.User` object
There is always `User` in `client.user` injected, so you can use all framework features from here.
```python
user = client.user

user.storage # for config files, resources and any type of storage
user.storage.resources = {} # any temporary resources, like game sessions or states
data = storage.load_json('fridge.json')
storage.write_json('fridge.json', {'food': ['apples', 'pizza']})

user.schedule: scheduler.Scheduler # advised to use for periodical tasks of individual users (in-module usage)
user.schedule.daily(datetime.time(hour=7, minute=58), wake_up)
```

### Decorators
You can apply decorators to `execute()` method of command or listener.
```python
import src.decorators as decorators

class ExampleListener(BaseListener):

    @decorators.is_private
    async def execute(self, c: pyrogram.Client, m: pyrogram.types.Message):
        await m.reply('I reply only in private messages!')
```
```python
    @decorators.is_group
    @decorators.for_id(2405)
    async def execute(self, c: pyrogram.Client, m: pyrogram.types.Message):
        await m.reply('I reply only in public chats to user with id 2405!')
```