# my_KOF97_Agent
这是一个基于强化学习的拳皇97游戏AI训练系统。让我为您分析主要组件：

### 1. 核心组件

### 1.1 环境封装 (kof_environment.py)

```python
class Environment(gym.Env):
    def __init__(self, env_id, roms_path, difficulty=3, frame_ratio=3, frames_per_step=3...):

```

- 基于OpenAI Gym的游戏环境封装
- 处理游戏状态、动作执行和奖励计算
- 管理游戏画面帧和内存状态

### 1.2 动作系统 ([actions.py](http://actions.py/))

```python
class Actions(Enum):
    # 定义了所有可能的游戏操作
    P1_UP = Action(':edge:joy:JOY1', 'P1 Up')
    P1_DOWN = Action(':edge:joy:JOY1', 'P1 Down')
    # ...

```

- 定义了所有可能的游戏操作(上下左右、攻击按键等)
- 为两个玩家分别定义了控制接口

### 1.3 内存地址管理 ([address.py](http://address.py/))

```python
def setup_memory_addresses():
    memory = {
        "healthP1": Address('0x108239', 's8'),
        "1P_x": Address('0x108118', 'u16'),
        # ...
    }

```

- 定义了游戏中需要监控的内存地址
- 包括生命值、位置、状态等关键信息

### 2. 训练系统

### 2.1 基础训练框架 ([baseline.py](http://baseline.py/))

```python
def main():
    model = PPO(
        ActorCriticResnetPolicy,
        env,
        device="cuda",
        verbose=1,
        # ...
    )

```

- 使用PPO(Proximal Policy Optimization)算法进行训练
- 支持ResNet策略网络
- 包含学习率调度和奖励裁剪

### 2.2 环境包装器 (king_of_fight_custom_wrapper.py)

```python
class KoFCustomWrapper(gym.Wrapper):
    def reward(self, info):
        # 计算奖励值
        damage_reward = ...
        distance_reward = ...

```

- 处理观察空间和动作空间
- 实现自定义奖励函数
- 管理帧堆叠和状态转换

### 3. 交互系统

### 3.1 键盘控制 (keyboard_play.py)

```python
def play(env, player=1, role="kyo", transpose=True, fps=30...):

```

- 支持人机对战
- 处理键盘输入
- 显示游戏画面

### 3.2 连招系统 ([comble.py](http://comble.py/))

```python
comble_kyo = {
    5: [[1, 8], [2, 8]]+[[5, 2]]*5,
    6: [[3, 8], [2, 8]]+[[6, 3]]*5,
    # ...
}

```

- 定义了各角色的连招动作序列
- 支持不同的攻击组合

### 4. 监控系统 ([monitor.py](http://monitor.py/))

```python
class Monitor(gym.Wrapper):
    def __init__(self, env, filename=None...):

```

- 记录训练过程中的数据
- 支持TensorBoard可视化
- 保存训练日志

### 主要依赖库

1. **游戏模拟器相关**:
- MAMEToolkit - 游戏模拟器接口
1. **强化学习框架**:
- gymnasium/gym - 强化学习环境接口
- stable-baselines3 - 强化学习算法实现
1. **深度学习**:
- PyTorch - 深度学习框架
- numpy - 数值计算
1. **可视化和监控**:
- pygame - 游戏显示
- tensorboard - 训练过程可视化

这个项目展示了一个完整的游戏AI训练系统，包含了从底层游戏控制到高层策略学习的各个层面。