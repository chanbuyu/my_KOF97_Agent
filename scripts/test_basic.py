from MAMEToolkit.emulator import Emulator
from actions import Actions
from address import setup_memory_addresses
import time

def test_basic_functions():
    try:
        # 1. 初始化模拟器
        roms_path = "../roms"  # ROM文件的相对路径
        game_id = "kof97"
        emulator = Emulator(roms_path, game_id)
        
        # 2. 设置内存地址监控
        memory = setup_memory_addresses()
        emulator.setup_memory_addresses(memory)
        
        print("模拟器初始化成功!")
        
        # 3. 测试基本操作
        print("\n开始测试基本操作...")
        
        # 投币并开始游戏
        emulator.step([Actions.COIN_P1.value])
        time.sleep(1)
        emulator.step([Actions.P1_START.value])
        time.sleep(2)
        
        # 4. 读取并显示内存数据
        print("\n读取内存数据:")
        data = emulator.step([])
        print(f"游戏状态: {data['playing']}")
        print(f"剩余时间: {data['time']}")
        print(f"P1血量: {data['healthP1']}")
        print(f"P2血量: {data['healthP2']}")
        
        # 5. 测试基本移动
        print("\n测试基本移动...")
        movements = [
            (Actions.P1_RIGHT.value, "右移"),
            (Actions.P1_LEFT.value, "左移"),
            (Actions.P1_UP.value, "上跳"),
            (Actions.P1_DOWN.value, "下蹲")
        ]
        
        for action, name in movements:
            print(f"执行动作: {name}")
            emulator.step([action])
            time.sleep(0.5)
        
        # 6. 测试攻击按键
        print("\n测试攻击按键...")
        attacks = [
            (Actions.P1_A.value, "A键"),
            (Actions.P1_B.value, "B键"),
            (Actions.P1_C.value, "C键"),
            (Actions.P1_D.value, "D键")
        ]
        
        for action, name in attacks:
            print(f"执行动作: {name}")
            emulator.step([action])
            time.sleep(0.5)
            
        print("\n测试完成!")
        
    except Exception as e:
        print(f"测试过程中出现错误: {str(e)}")
    finally:
        # 关闭模拟器
        if 'emulator' in locals():
            emulator.close()

if __name__ == "__main__":
    test_basic_functions()
