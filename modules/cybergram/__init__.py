from .reboot import RebootCommand, ExitCommand
from .schedule import ScheduleCommand
from .exec_command import ExecCommand, AExecCommand, EvalCommand, AEvalCommand
from .modules import LoadModuleCommand, UnloadModuleCommand, ModulesCommand, ModuleCommand

commands = [RebootCommand, ScheduleCommand, ExecCommand, AExecCommand, EvalCommand, AEvalCommand,
            LoadModuleCommand, UnloadModuleCommand, ModulesCommand, ModuleCommand, ExitCommand
    ]
listeners = []