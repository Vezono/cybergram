from .reboot import RebootCommand
from .schedule import ScheduleCommand
from .exec_command import ExecCommand, AExecCommand

commands = [RebootCommand, ScheduleCommand, ExecCommand, AExecCommand]
listeners = []