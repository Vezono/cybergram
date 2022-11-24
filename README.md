# cybergram v0.2.1-beta
## Authors
Made by *vezono* and *Teacater*

## Configuration
First, you need to create `accounts.toml`, which contains list of accounts and their settings.
```toml
# accounts.toml
[user1]
name = "user1"

[user2]
name = "user2"
enabled = ["example", "sugar"] # only "example" and "sugar" modules will be used by this user

[user3]
name = "user3"
disabled = ["apple"] # all modules except "apple" module will be used
```

After that, you need to fill out `accounts/<user>/config.json`. Other modules will ask for further configuration in this file along the way.
```json
{
    "api_id": 813029, 
    "api_hash": "d0e84cf0acdedf400a2c4956300664d4"
}
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