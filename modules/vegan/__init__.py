from .listeners.StartVeganListener import StartVeganListener
from .listeners.StopVeganListener import StopVeganListener
from .listeners.ProfileVeganListener import ProfileVeganListener

from .commands.vegan_command import VeganCommand
from .commands.vegan_plan_command import VeganPlanCommand
from .commands.vegan_battle_command import VeganBattleCommand
from .commands.vegan_item_command import VeganItemCommand
from .commands.info_command import VeganInfoCommand
from .commands.va_info_command import VAInfoCommand

commands = [VeganCommand, VeganPlanCommand, VeganBattleCommand, VeganItemCommand, VeganInfoCommand,
            VAInfoCommand]
listeners = [StopVeganListener, StartVeganListener, ProfileVeganListener]