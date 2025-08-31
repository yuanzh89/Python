from enum import Enum, IntEnum, StrEnum, unique, auto

@unique
class TrafficLightEnum(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

current_light = TrafficLightEnum.RED
print(current_light)
print(current_light.name)
print(current_light.value)

@unique
class ErrorCode(Enum):
    NOT_FOUND = auto()
    UNAUTHORIZED = auto()
    FORBIDDEN = auto()

print(ErrorCode.NOT_FOUND.value)
print(ErrorCode.UNAUTHORIZED.value)
print(ErrorCode.FORBIDDEN.value)

@unique
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

if Priority.HIGH > Priority.MEDIUM:
    print("High priority is higher than medium priority.")

print(["low", "medium", "high"][Priority.LOW - 1])

@unique
class Color(StrEnum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def print_color(color: Color):
    print(f"The color is {color}.")

if Color.RED == "red":
    print("String match!")