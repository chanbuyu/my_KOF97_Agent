
MAMEToolkit版本是Version: 1.1.0


1. **添加MAME到PATH**（推荐）：

```bash
# 将/usr/games添加到PATH
export PATH=$PATH:/usr/games

# 验证MAME是否可用
which mame
mame --version

```


创建测试文件
/root/my_KOF97_Agent/test_mame.py


(game_AI) root@autodl-container-b9b842b3fc-589e6765:~/my_KOF97_Agent# python test_mame.py 
开始测试MAME安装...
ROM路径: /root/my_KOF97_Agent/roms
环境ID: 1425
尝试启动MAME模拟器...
ALSA lib seq_hw.c:457:(snd_seq_hw_open) open /dev/snd/seq failed: No such file or directory
MAME模拟器启动成功!

内存读取测试:
游戏状态: 0
玩家1血量: 0
玩家2血量: 0
游戏时间: 50
玩家1位置: (0, 0)
玩家2位置: (0, 0)

MAME模拟器关闭成功!