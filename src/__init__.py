
from src.Registry import Registry
from src.commands.boot import BootModule

from src.commands.ping_command import PingCommand
from src.commands.silent_chat_info_command import SilentChatInfoCommand
from src.commands.silent_user_info_command import SilentUserInfoCommand
from src.commands.vegan_plan_command import VeganPlanCommand
from src.commands.wolfram_command import WolframCommand
from src.commands.message_info_command import MessageInfoCommand
from src.commands.vegan_command import VeganCommand
from src.commands.dick_command import DickCommand
from src.commands.doeb_command import DoebCommand
from src.commands.doeb_cancel_command import DoebCancelCommand

from src.listeners.CheckListener import CheckListener
from src.listeners.StopVeganListener import StopVeganListener
from src.listeners.StartVeganListener import StartVeganListener


def get_registry(config: dict) -> Registry:
    registry = Registry()
    registry.register_command(BootModule())
    
    registry.register_command(PingCommand())
    registry.register_command(SilentChatInfoCommand())
    registry.register_command(SilentUserInfoCommand())
    registry.register_command(WolframCommand(config["wolfram"]))
    registry.register_command(MessageInfoCommand())
    registry.register_command(VeganCommand())
    registry.register_command(VeganPlanCommand())
    registry.register_command(DickCommand())
    registry.register_command(DoebCommand())
    registry.register_command(DoebCancelCommand())
    registry.register_listener(CheckListener())
    registry.register_listener(StopVeganListener())
    registry.register_listener(StartVeganListener())
    return registry
