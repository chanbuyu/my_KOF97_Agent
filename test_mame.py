import os
from MAMEToolkit.emulator import Emulator, Address
import time
import random

def setup_memory_addresses():
    """设置需要监控的内存地址"""
    return {
        # 游戏状态
        "playing": Address('0x108441', 'u8'),
        
        # 玩家1状态
        "healthP1": Address('0x108239', 'u8'),
        "1P_x": Address('0x108118', 'u16'),
        "1P_y": Address('0x108120', 'u16'),
        "1P_input": Address('0x300000', 'u8'),
        "1P_AttackStatus": Address('0x108172', 'u32'),
        "1P_Status": Address('0x108171', 'u8'),
        "1P_StatusExtra": Address('0x108173', 'u8'),
        "1P_PowerValue": Address('0x108293', 'u8'),
        "1P_PowerStatus": Address('0x108294', 'u8'),
        
        # 玩家2状态
        "healthP2": Address('0x108439', 'u8'),
        "2P_x": Address('0x108318', 'u16'),
        "2P_y": Address('0x108320', 'u16'),
        "2P_input": Address('0x300001', 'u8'),
        "2P_AttackStatus": Address('0x108372', 'u32'),
        "2P_Status": Address('0x108371', 'u8'),
        "2P_StatusExtra": Address('0x108373', 'u8'),
        "2P_PowerValue": Address('0x108493', 'u8'),
        "2P_PowerStatus": Address('0x108494', 'u8'),
        
        # 其他游戏信息
        "time": Address('0x10A83C', 'u8'),
    }

def test_mame():
    """测试MAME模拟器是否正确安装和运行"""
    try:
        print("开始测试MAME安装...")
        
        # 设置虚拟显示 (使用显示端口 99)
        display_num = 99
        os.environ["DISPLAY"] = f":{display_num}"
        
        # 清理可能存在的旧锁文件
        lock_file = f"/tmp/.X{display_num}-lock"
        if os.path.exists(lock_file):
            os.remove(lock_file)
            
        os.system(f"Xvfb :{display_num} -screen 0 1024x768x24 &")
        time.sleep(2)  # 等待Xvfb启动
        
        # 生成随机env_id
        env_id = random.randint(1000, 9999)
        
        # 配置MAME
        roms_path = os.path.join(os.getcwd(), "roms")  # 使用绝对路径
        game_id = "kof97"   # 游戏ID
        memory_addresses = setup_memory_addresses()
        
        print(f"ROM路径: {roms_path}")
        print(f"环境ID: {env_id}")
        print("尝试启动MAME模拟器...")
        
        # 创建Emulator实例
        emu = Emulator(env_id, roms_path, game_id, memory_addresses)
        print("MAME模拟器启动成功!")
        time.sleep(2)  # 等待一下确保模拟器完全启动
        
        # 读取一些内存值进行测试
        data = emu.step([])  # 空动作列表
        print("\n内存读取测试:")
        print(f"游戏状态: {data['playing']}")
        print(f"玩家1血量: {data['healthP1']}")
        print(f"玩家2血量: {data['healthP2']}")
        print(f"游戏时间: {data['time']}")
        print(f"玩家1位置: ({data['1P_x']}, {data['1P_y']})")
        print(f"玩家2位置: ({data['2P_x']}, {data['2P_y']})")
        
        # 关闭模拟器
        emu.close()
        print("\nMAME模拟器关闭成功!")
        
        # 清理虚拟显示
        os.system(f"pkill -f 'Xvfb :{display_num}'")
        
        return True
        
    except Exception as e:
        print(f"测试失败: {str(e)}")
        os.system(f"pkill -f 'Xvfb :{display_num}'")  # 确保清理虚拟显示
        return False

if __name__ == "__main__":
    test_mame() 