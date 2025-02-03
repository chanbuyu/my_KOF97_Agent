from MAMEToolkit.emulator import Address

def setup_memory_addresses():
    return {
        "playing": Address('0x108441', 'u8'),
        "time": Address('0x108924', 'u8'),
        "healthP1": Address('0x108239', 'u8'),
        "healthP2": Address('0x108439', 'u8'),
        # 添加更多需要监控的内存地址
    }
