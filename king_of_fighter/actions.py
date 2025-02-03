from enum import Enum
from MAMEToolkit.emulator import Action

class Actions(Enum):
    # 基本操作
    COIN_P1 = Action(':edge:coin:Coin 1')
    P1_START = Action(':edge:start:1 Player Start')
    
    # 方向键
    P1_UP = Action(':edge:joy:JOY1', 'P1 Up')
    P1_DOWN = Action(':edge:joy:JOY1', 'P1 Down')
    P1_LEFT = Action(':edge:joy:JOY1', 'P1 Left')
    P1_RIGHT = Action(':edge:joy:JOY1', 'P1 Right')
    
    # 攻击键
    P1_A = Action(':edge:joy:JOY1', 'P1 Button 1')
    P1_B = Action(':edge:joy:JOY1', 'P1 Button 2')
    P1_C = Action(':edge:joy:JOY1', 'P1 Button 3')
    P1_D = Action(':edge:joy:JOY1', 'P1 Button 4')
