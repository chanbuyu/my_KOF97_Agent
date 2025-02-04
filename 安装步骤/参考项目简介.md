
## 项目目录结构

```
.
├── .gitignore
├── code_analyzer.py
├── code_analyzer_manual.py
├── code_documentation.md
├── env
│   ├── game_AI.yaml
│   └── packages.txt
├── failed_files.txt
├── figures
│   ├── opt.png
│   └── xmoba.png
├── generate_tree.py
├── king_of_fighter
│   ├── actions.py
│   ├── address.py
│   ├── baseline.py
│   ├── comble.py
│   ├── debug.py
│   ├── keyboard_play.py
│   ├── king_of_fight_custom_wrapper.py
│   ├── kof_environment.py
│   ├── monitor.py
│   ├── ppo
│   │   ├── base_class.py
│   │   ├── cnn_policy.py
│   │   ├── dummy_vec_env.py
│   │   ├── on_policy_algorithm.py
│   │   ├── ppo.py
│   │   ├── resnet_customer.py
│   │   ├── resnet_policy.py
│   │   └── torch_layers.py
│   ├── steps.py
│   └── visualize.py
├── README.md
├── roms
│   ├── kof97
│   │   ├── 000-lo.lo
│   │   ├── 232-c1.bin
│   │   ├── 232-c1.c1
│   │   ├── 232-c2.bin
│   │   ├── 232-c2.c2
│   │   ├── 232-c3.bin
│   │   ├── 232-c3.c3
│   │   ├── 232-c4.bin
│   │   ├── 232-c4.c4
│   │   ├── 232-c5.bin
│   │   ├── 232-c5.c5
│   │   ├── 232-c6.bin
│   │   ├── 232-c6.c6
│   │   ├── 232-m1.bin
│   │   ├── 232-m1.m1
│   │   ├── 232-p1.bin
│   │   ├── 232-p1.p1
│   │   ├── 232-p2.bin
│   │   ├── 232-p2.sp2
│   │   ├── 232-s1.bin
│   │   ├── 232-s1.s1
│   │   ├── 232-v1.bin
│   │   ├── 232-v1.v1
│   │   ├── 232-v2.bin
│   │   ├── 232-v2.v2
│   │   ├── 232-v3.bin
│   │   ├── 232-v3.v3
│   │   ├── asia-s3.rom
│   │   ├── japan-j3.bin
│   │   ├── readme.html
│   │   ├── sfix.sfix
│   │   ├── sm1.sm1
│   │   ├── sp-1v1_3db8c.bin
│   │   ├── sp-45.sp1
│   │   ├── sp-e.sp1
│   │   ├── sp-j2.sp1
│   │   ├── sp-s.sp1
│   │   ├── sp-s2.sp1
│   │   ├── sp1.jipan.1024
│   │   ├── uni-bios_1_0.rom
│   │   ├── uni-bios_1_1.rom
│   │   ├── uni-bios_1_2.rom
│   │   ├── uni-bios_1_2o.rom
│   │   ├── uni-bios_1_3.rom
│   │   ├── uni-bios_2_0.rom
│   │   ├── uni-bios_2_1.rom
│   │   ├── uni-bios_2_2.rom
│   │   ├── uni-bios_2_3.rom
│   │   ├── uni-bios_2_3o.rom
│   │   ├── usa_2slt.bin
│   │   └── vs-bios.rom
│   └── sfiii3
│       ├── sfiii3-simm1.0
│       ├── sfiii3-simm1.1
│       ├── sfiii3-simm1.2
│       ├── sfiii3-simm1.3
│       ├── sfiii3-simm2.0
│       ├── sfiii3-simm2.1
│       ├── sfiii3-simm2.2
│       ├── sfiii3-simm2.3
│       ├── sfiii3-simm3.0
│       ├── sfiii3-simm3.1
│       ├── sfiii3-simm3.2
│       ├── sfiii3-simm3.3
│       ├── sfiii3-simm3.4
│       ├── sfiii3-simm3.5
│       ├── sfiii3-simm3.6
│       ├── sfiii3-simm3.7
│       ├── sfiii3-simm4.0
│       ├── sfiii3-simm4.1
│       ├── sfiii3-simm4.2
│       ├── sfiii3-simm4.3
│       ├── sfiii3-simm4.4
│       ├── sfiii3-simm4.5
│       ├── sfiii3-simm4.6
│       ├── sfiii3-simm4.7
│       ├── sfiii3-simm5.0
│       ├── sfiii3-simm5.1
│       ├── sfiii3-simm5.2
│       ├── sfiii3-simm5.3
│       ├── sfiii3-simm5.4
│       ├── sfiii3-simm5.5
│       ├── sfiii3-simm5.6
│       ├── sfiii3-simm5.7
│       ├── sfiii3-simm6.0
│       ├── sfiii3-simm6.1
│       ├── sfiii3-simm6.2
│       ├── sfiii3-simm6.3
│       ├── sfiii3-simm6.4
│       ├── sfiii3-simm6.5
│       ├── sfiii3-simm6.6
│       ├── sfiii3-simm6.7
│       └── sfiii3_japan_nocd.29f400.u2
├── scripts
│   ├── run.sh
│   └── train.sh
└── status
    ├── iori_2p_started
    ├── kyo_2p_started
    ├── kyo_2p_started_play
    ├── mai_2p_started
    ├── wait_for_fight_start_stage_01
    └── wait_for_fight_start_stage_02
```
## code_analyzer.py

文件路径: `code_analyzer.py`

### AI分析说明



该代码调用了以下库：

1. **os** - 用于操作系统相关功能（文件路径操作、存在性检查）
2. **pathlib.Path** - 处理文件路径和目录遍历（通过rglob查找.py文件）
3. **time** - 处理延迟和重试等待（sleep）
4. **requests** - 核心HTTP请求库（用于向DMX API发送POST请求）
5. **json** - 处理API响应数据的解析（解析流式响应）
6. **tqdm** - 显示进度条（分析文件时的进度可视化）
7. **sys** - 处理命令行参数（获取项目根目录和重试模式）

代码主要功能是通过DMX API分析指定目录下的Python文件，生成代码说明文档。核心流程包含：
1. 递归扫描目录获取.py文件列表
2. 使用requests库流式调用DMX API进行代码分析
3. 处理JSON格式的API响应
4. 用tqdm显示分析进度条
5. 支持失败重试机制（通过time.sleep实现延迟）
6. 生成Markdown格式的文档并记录失败文件

---

## code_analyzer_manual.py

文件路径: `code_analyzer_manual.py`

### AI分析说明



这段代码调用了以下库：

1. **os** - 用于操作系统相关操作（文件路径处理、文件存在性检查）
2. **pathlib.Path** - 提供面向对象的文件路径操作
3. **time** - 处理时间相关操作（等待间隔）
4. **requests** - 发送HTTP请求与DMX API交互
5. **json** - 处理API返回的JSON格式数据
6. **tqdm** - 显示命令行进度条
7. **sys** - 处理命令行参数和系统退出

代码核心功能是通过DMX API批量分析代码文件，自动生成说明文档。主要流程：
1. 读取指定代码文件
2. 通过requests库调用流式API获取分析结果
3. 使用json解析响应数据
4. 用tqdm显示处理进度
5. 将结果写入Markdown文档
6. 支持失败重试和断点续处理

特殊处理：
- 流式响应解析（处理data:前缀和[DONE]标记）
- 自动过滤<think>标签内容
- 失败文件记录重试机制
- 支持命令行参数和代码内指定文件两种模式

---

## generate_tree.py

文件路径: `generate_tree.py`

### AI分析说明



该代码调用了以下三个标准库：

1. `pathlib` 的 `Path`：用于处理文件路径和目录操作
2. `io` 的 `StringIO`：用于创建内存文本缓冲区
3. `sys`：用于系统相关操作（如修改标准输出编码）

主要功能说明：
该脚本通过递归遍历目录生成树状结构，自动跳过.git目录，支持两种输出方式：
1. 控制台打印（使用UTF-8编码，特别处理Windows系统）
2. 追加写入Markdown文件（生成带代码块的目录结构文档）

核心实现：
- 使用`pathlib`进行路径操作和目录遍历
- 通过递归函数`generate_tree`构建树形结构
- 利用`sys.stdout.reconfigure`确保Windows控制台正确显示UTF-8字符
- 使用`io.StringIO`暂存输出内容，最后批量写入Markdown文件

---

## king_of_fighter\actions.py

文件路径: `king_of_fighter\actions.py`

### AI分析说明



该代码定义了一个枚举类 `Actions`，用于管理游戏《拳皇》的模拟器操作指令。主要调用了以下两个库：

1. **`enum` 库的 `Enum` 类**  
   用于创建枚举类型，使每个动作（如投币、移动、攻击）成为预定义的常量成员。

2. **`MAMEToolkit.emulator` 库的 `Action` 类**  
   用于封装每个动作的底层参数：  
   - 第1个参数是 **Lua引擎端口**（如 `:edge:joy:JOY1` 表示玩家1摇杆信号）  
   - 第2个参数是 **动作名称**（如 `P1 Button 1` 对应玩家1的A键）

### 代码功能分段
- **初始化操作**：投币（`COIN_P1/P2`）、开始游戏（`P1_START/P2_START`）  
- **移动操作**：玩家1/2的上下左右（通过 `JOY1/JOY2` 区分摇杆）  
- **战斗按键**：玩家1/2的A/B/C/D四个攻击键（对应按钮1-4）

该枚举类常用于游戏模拟器环境（如MAME）中，将高层操作映射到底层Lua脚本指令。

---

## king_of_fighter\address.py

文件路径: `king_of_fighter\address.py`

### AI分析说明



这段代码调用了 `MAMEToolkit` 库中的 `Address` 类（来自其 `emulator` 模块），用于定义《拳皇》游戏的内存地址映射。其核心功能是通过 `setup_memory_addresses` 函数返回一个包含游戏状态监测点的字典，具体包括：

1. **全局状态**  
   - 游戏运行状态（`playing`）
   - 对战倒计时（`time`）

2. **玩家1（1P）数据**  
   - 实时输入（`1P_input`）、连帧输入（`1P_2Frame`）
   - 血量（`healthP1`）、坐标（`1P_x/y`）
   - 攻击状态（`AttackStatus`）、角色状态（`Status/StatusExtra`）
   - 能量值（`PowerValue`）和能量槽状态（`PowerStatus`）

3. **玩家2（2P）数据**  
   - 结构与1P完全对称（如 `2P_input`, `healthP2` 等）

每个地址通过 `Address(内存地址, 数据类型)` 定义，数据类型涵盖 `u8`（无符号字节）、`s8`（有符号字节）、`u16`（双字节）、`u32`（四字节），用于精确读取模拟器内存中的游戏状态。

---

## king_of_fighter\baseline.py

文件路径: `king_of_fighter\baseline.py`

### AI分析说明



该代码是一个基于强化学习的训练程序，用于训练AI玩《拳皇》（King of Fighters）游戏。以下是核心说明及调用的库：

---

### **调用的第三方库**
1. **retro**：用于创建复古游戏模拟环境（通过`gym-retro`库）。
2. **stable_baselines3**：  
   - `CheckpointCallback`：保存模型训练检查点。  
   - `SubprocVecEnv`（代码中导入但未显式使用）：多进程并行环境支持。
3. **argparse**：解析命令行参数（如指定训练角色`--role`）。

---

### **代码功能说明**
1. **环境初始化**  
   - 使用自定义的`Environment`和`KoFCustomWrapper`包装游戏环境，处理角色动作和观测。
   - 通过`Monitor`记录训练数据。
   - 使用`Xvfb`虚拟显示服务器（通过`os.system`调用）以无界面模式运行。

2. **PPO算法配置**  
   - 使用自定义的`PPO`实现（从`ppo.ppo`导入，而非`stable_baselines3`原版）。
   - 策略网络采用`ActorCriticResnetPolicy`（基于ResNet的自定义策略）。
   - 学习率（`lr_schedule`）和梯度裁剪范围（`clip_range_schedule`）使用线性衰减调度。

3. **训练流程**  
   - 通过`CheckpointCallback`定期保存模型（间隔5000步）。
   - 使用`tensorboard`记录训练日志。
   - 最终模型保存为`trained_models/ppo_{role}_resnet_2p_final.zip`。

---

### **其他依赖**
- **用户自定义模块**：  
  `kof_environment`、`king_of_fight_custom_wrapper`、`ppo`中的策略和模型实现（如`ActorCriticResnetPolicy`）。
- **系统工具**：  
  依赖`Xvfb`提供虚拟显示支持（非Python库）。

---

### **总结**
代码通过结合`retro`游戏环境与自定义PPO实现，训练一个基于ResNet策略的AI模型，支持多进程环境（潜在功能）和模型检查点保存，适用于《拳皇》游戏的强化学习任务。

---

## king_of_fighter\comble.py

文件路径: `king_of_fighter\comble.py`

### AI分析说明



该代码仅调用了 `numpy` 库（以别名 `np` 导入），主要用于处理数组的变形操作。

### 代码功能说明：
1. **定义基础招式指令**  
   `comble_base` 字典存储基础动作的指令序列（如前进、防御），每个键值对代表一个招式编号及其对应的二维坐标序列（如 `[方向键, 按键]`）。

2. **定义角色专属连招**  
   `comble_kyo` 字典存储角色（如 Kyo）的复杂连招指令，通过 `numpy` 进行数组变形：  
   - `np.array(v)` 将列表转为 NumPy 数组  
   - `.reshape(-1, 1, 2)` 调整数组维度为 (步骤数, 1, 2)  
   - `.repeat(2, 1)` 在第1轴（中间维度）复制数据2次  
   - `.reshape(-1, 2)` 最终压平成 (N, 2) 的指令序列  
   （可能用于扩展指令的持续时间或兼容游戏引擎输入）

3. **方向映射关系**  
   `reverse` 字典定义了键位反转逻辑（如将编号1映射到3），推测用于处理角色左右镜像反转时的输入适配。

### 典型应用场景：
此代码疑似为格斗游戏（如《拳皇》）的连招指令系统，通过预定义的指令序列实现角色招式自动化输入。

---

## king_of_fighter\debug.py

文件路径: `king_of_fighter\debug.py`

### AI分析说明



这段代码调用了以下库和模块：

---

### **1. 第三方库**
- **`numpy` (np)**: 用于数值计算。
- **`argparse`**: 解析命令行参数（如 `--role`, `--player`）。
- **`random`**: 生成随机数。
- **`copy.deepcopy`**: 深度复制对象。

---

### **2. 项目自定义模块**
- **`kof_environment.Environment`**: 创建KOF游戏环境的核心类。
- **`monitor.Monitor`**: 监控游戏运行状态（如胜率、帧数）。
- **`king_of_fight_custom_wrapper.KoFCustomWrapper`**: 自定义环境封装，处理动作空间和观测。
- **`keyboard_play.play`**: 控制游戏交互和键盘输入。
- **`ppo.PPO`**: 实现PPO强化学习算法的模型类。
- **`ppo.resnet_policy.ActorCriticResnetPolicy`**: 基于ResNet的策略网络。
- **`baseline.lr_schedule` 和 `baseline.clip_range_schedule`**: 定义学习率和梯度裁剪的策略。

---

### **3. 系统级操作**
- **`os`**: 管理环境变量（如 `DISPLAY`）和文件路径。
- **`os.system`**: 调用系统命令启动虚拟显示服务器 `Xvfb`（用于无头渲染）。

---

### **代码功能概述**
1. **环境初始化**  
   - 通过 `make_env` 创建游戏环境，整合 `Environment`、`KoFCustomWrapper` 和 `Monitor`。
   - 使用命令行参数设置角色（如 `kyo`、`mai`）和玩家编号（1或2）。

2. **模型加载**  
   - 从预训练文件加载PPO模型（`ppo_{role}_resnet_2p_100000_steps.zip`）。

3. **游戏运行**  
   - 调用 `play` 函数启动游戏，结合环境封装和模型进行交互。

---

### **依赖关键点**
- **强化学习框架**: 使用自定义PPO实现（非Stable-Baselines3等标准库）。
- **显示依赖**: 依赖 `Xvfb` 虚拟显示（Linux环境）和 `DISPLAY` 变量配置。

---

## king_of_fighter\keyboard_play.py

文件路径: `king_of_fighter\keyboard_play.py`

### AI分析说明



该代码调用了以下主要库：

1. **gym**：OpenAI Gym强化学习环境库，用于创建和管理游戏环境
2. **pygame**：处理游戏界面渲染、键盘输入和事件循环
3. **matplotlib**：数据可视化（通过TkAgg后端）
4. **argparse**：命令行参数解析
5. **numpy**：数组处理（通过隐式调用）
6. **torch**：PyTorch深度学习框架，用于神经网络推理
7. **stable_baselines3**：强化学习算法实现，包含：
   - common.preprocessing：观测空间处理
   - common.vec_env：环境向量化
   - common.utils：张量转换工具
8. **gymnasium**：新版Gym API兼容接口

主要功能：
- 实现《拳皇》游戏的键盘控制玩法
- 包含玩家与AI对战逻辑（1P/2P模式）
- 使用PyTorch模型进行动作预测
- 通过Pygame渲染游戏画面并处理输入
- 支持连招组合（comble）系统
- 包含强化学习环境交互逻辑

代码核心是通过Pygame捕获键盘输入，结合预训练模型生成动作指令，控制游戏角色执行移动和攻击组合技，同时实时渲染游戏画面。

---

## king_of_fighter\king_of_fight_custom_wrapper.py

文件路径: `king_of_fighter\king_of_fight_custom_wrapper.py`

### AI分析说明



这段代码定义了一个名为`KoFCustomWrapper`的自定义强化学习环境封装类，主要用于处理《拳皇》游戏的观测和奖励机制。它调用了以下库：

### **调用的第三方库**
1. **`cv2` (OpenCV)**：用于图像处理（如灰度转换和下采样）。
2. **`gym` 和 `gymnasium`**：提供强化学习环境接口，定义动作空间（`Discrete`）和观测空间（`Box`）。
3. **`numpy` (np)**：处理图像堆叠和数值计算。
4. **`collections`**：使用`deque`实现帧堆叠（存储最近9帧图像）。
5. **`copy.deepcopy`**：深拷贝动作组合数据。
6. **`comble`（自定义模块）**：定义角色动作组合（如`comble_base`和`comble_mai`）。

---

### **代码核心功能**
1. **帧处理**  
   - 对原始图像下采样（`::2, ::2`）并堆叠最后9帧，生成112x160x3的观测张量（`_stack_observation`）。
   - 使用OpenCV将RGB帧转为灰度（`cv2.COLOR_RGB2GRAY`）。

2. **动作管理**  
   - 通过`comble`模块加载预定义连招动作，支持角色（如`role="mai"`）的特定连招。
   - 处理动作翻转（`flip`方法）以适应角色朝向变化。

3. **奖励计算**  
   - 基于双方血量变化（`damage_reward`）、距离惩罚（`distance_reward`）设计奖励函数。
   - 归一化奖励值（`reward_coeff=3.0`）。

4. **环境交互**  
   - 封装`reset`和`step`方法，兼容单人和双人模式（`mode='computer_2p'`）。
   - 通过帧堆叠和状态重置（`reset_round`）管理对局生命周期。

---

### **用途**
该代码用于训练强化学习模型在《拳皇》游戏中实现自动化对战，重点处理图像输入和动作连招的复杂逻辑。

---

## king_of_fighter\kof_environment.py

文件路径: `king_of_fighter\kof_environment.py`

### AI分析说明



这段代码实现了一个基于《拳皇97》游戏的强化学习环境，主要调用了以下库：

1. **核心第三方库**：
- `MAMEToolkit`：街机游戏模拟框架（从emulator子模块导入Emulator和Address类）
- `gym`：OpenAI的强化学习环境接口（继承gym.Env创建自定义环境）
- `torch`：PyTorch深度学习框架（用于随机种子设置）
- `numpy`：数值计算库

2. **Python标准库**：
- `random`：随机数生成
- `glob`：文件路径匹配
- `os`：操作系统接口

3. **项目内部模块**：
- `steps`：包含游戏流程控制函数（如start_game_2p等）
- `actions`：定义玩家动作枚举类Actions
- `address`：提供setup_memory_addresses内存地址配置

代码核心功能：
1. 通过MAMEToolkit连接游戏模拟器，实现帧数据获取和动作输入
2. 定义动作映射系统（index_to_move_action_p1/p2等函数将数字动作转换为游戏指令）
3. 实现Gym标准接口（reset/step/render等方法），支持强化学习算法训练
4. 包含游戏状态解析（血条、能量值、攻击状态等游戏数据提取）
5. 提供多模式控制（支持人机对战/双AI对战等不同模式）

环境特点：
- 支持帧跳过（frame_skip）和帧聚合（frames_per_step）优化性能
- 包含奖励计算系统（基于血量变化设计奖励机制）
- 实现游戏状态自动恢复/存档功能（通过machine().load()/save()）
- 支持多阶段游戏进度管理（stage参数控制）

---

## king_of_fighter\monitor.py

文件路径: `king_of_fighter\monitor.py`

### AI分析说明



这段代码实现了一个用于监控强化学习环境训练的模块，主要调用了以下库：

1. **标准库**：
   - `csv`：用于写入CSV格式的训练日志
   - `json`：处理JSON格式的元数据头
   - `os`：目录创建/路径操作
   - `time`：记录训练时间
   - `glob`：查找监控文件路径

2. **第三方库**：
   - `gymnasium`：提供强化学习环境接口（原OpenAI Gym的升级版）
   - `pandas`：用于加载和分析监控数据（`load_results`函数）
   - `torch.utils.tensorboard`：提供TensorBoard日志功能（虽然相关代码被注释，但已导入SummaryWriter）

代码核心是`Monitor`类，它继承自`gym.Wrapper`，主要功能：
- 记录每个episode的奖励（分玩家1/2）、步数、耗时等指标
- 通过`ResultsWriter`将数据写入CSV文件
- 支持TensorBoard日志记录（需取消注释相关代码）
- 提供结果加载分析接口（`load_results`函数）

该模块常用于强化学习训练过程的性能监控和数据收集。

---

## king_of_fighter\steps.py

文件路径: `king_of_fighter\steps.py`

### AI分析说明



该代码文件调用了以下库：
1. 从本地模块`actions`导入`Actions`类（from actions import Actions）

代码功能说明：
这是一个格斗游戏《拳皇》的自动化操作脚本，主要实现以下功能：
- 定义了多个游戏启动流程（单人模式、双人模式及特定角色选择）
- 每个流程返回由"等待时间"和"游戏操作"组成的指令序列
- 使用`Actions`枚举类表示游戏操作指令（如投币、开始、方向键、攻击键等）
- 所有等待时间通过`frame_ratio`参数进行帧率适配计算
- 包含不同角色选择路线的预设操作（如八神庵、不知火舞等）

代码结构特点：
1. 四个启动函数分别对应不同游戏模式：
   - start_game()：单人模式
   - start_game_2p()：双人模式
   - start_game_2p_mai()：双人模式+特定角色组合
   - start_game_2p_iori()：双人模式+八神庵组合
2. next_stage() 函数处理关卡切换操作
3. 每个操作步骤包含等待帧数和对应的游戏输入动作

---

## king_of_fighter\visualize.py

文件路径: `king_of_fighter\visualize.py`

### AI分析说明



这段代码主要用于实现《拳皇》游戏的强化学习训练与可视化测试。以下是对其调用库的说明：

### 调用的第三方库：
1. **`numpy`**（导入为 `np`）  
   用于数值计算，处理数组和矩阵操作。

---

### 调用的Python标准库：
1. **`random`**  
   生成随机数，用于决策或初始化。
2. **`copy`**（特别是 `deepcopy`）  
   创建对象的深拷贝，避免数据修改时的副作用。
3. **`os`**  
   操作系统交互功能，如设置环境变量（`DISPLAY`）、执行系统命令（启动虚拟显示器 `Xvfb`）。

---

### 调用的自定义模块：
1. **`kof_environment`** 中的 `Environment`  
   定义游戏环境的核心逻辑，如状态获取和动作执行。
2. **`monitor`** 中的 `Monitor`  
   监控游戏运行状态，可能用于记录训练数据或调试。
3. **`king_of_fight_custom_wrapper`** 中的 `KoFCustomWrapper`  
   对原始环境进行封装，扩展角色控制或状态预处理功能。
4. **`keyboard_play`** 中的 `play_2p`  
   实现键盘控制的游戏对战逻辑。
5. **`ppo.ppo`** 中的 `PPO`  
   实现近端策略优化（PPO）算法，用于训练强化学习模型。
6. **`baseline`** 中的 `ActorCriticCnnPolicy`, `lr_schedule`, `clip_range_schedule`  
   定义策略网络结构和学习率/梯度裁剪的调度方法。

---

### 其他依赖：
- **Xvfb**（通过 `os.system` 调用）  
  虚拟显示服务器，用于无界面环境下的图形渲染（非Python库，但代码中通过系统命令启动）。

---

### 主要功能：
1. 通过 `make_env` 创建自定义游戏环境，结合 `KoFCustomWrapper` 和 `Monitor` 扩展功能。
2. 使用 `PPO` 算法加载或初始化模型，配置训练参数（如学习率、批次大小）。
3. 调用 `play_2p` 启动双人对战测试，结合模型推理与键盘控制。

---

## king_of_fighter\ppo\base_class.py

文件路径: `king_of_fighter\ppo\base_class.py`

### AI分析说明



该代码是强化学习算法的基础抽象类，主要调用了以下库：

1. **标准库**：
   - `io`：输入输出操作
   - `pathlib`：文件路径处理
   - `time`：时间相关功能
   - `warnings`：警告处理
   - `abc`：抽象基类（含`ABC`和`abstractmethod`）
   - `collections.deque`：双端队列数据结构
   - `typing`：类型注解支持

2. **第三方库**：
   - `gymnasium` (别名为 `gym`)：强化学习环境接口
   - `numpy` (别名为 `np`)：数值计算
   - `torch` (别名为 `th`)：PyTorch 深度学习框架
   - `stable_baselines3`：提供 RL 算法实现及相关工具，包含多个子模块：
     - `common` 下的 `utils`, `callbacks`, `env_util`, `logger`, `monitor`, `noise`, `policies`, `preprocessing`, `save_util`, `type_aliases`, `vec_env` 等
     - `common.vec_env` 中的 `VecEnv`, `VecNormalize`, `VecTransposeImage` 等环境包装器

3. **本地模块**：
   - `dummy_vec_env.DummyVecEnv`：通过相对导入的自定义向量化环境实现

代码核心功能包括环境包装、策略定义、回调机制、模型保存/加载等，是 Stable Baselines3 框架中算法的基础实现。

---

## king_of_fighter\ppo\cnn_policy.py

文件路径: `king_of_fighter\ppo\cnn_policy.py`

### AI分析说明



该代码实现了一个基于CNN的Actor-Critic策略类，主要用于PPO等强化学习算法。以下是调用的主要库及关键说明：

---

### **调用的第三方库**
1. **PyTorch (`torch`)**
   - 用于构建神经网络（`nn.Module`）、优化器（`th.optim.Adam`）和张量计算。
   - 关键模块：`torch.nn`, `torch.optim`.

2. **NumPy (`numpy`)**
   - 数值计算和数组操作。

3. **Gymnasium (`gymnasium`)**
   - 提供强化学习环境接口（`spaces` 定义观测和动作空间）。

4. **Stable Baselines3 (`stable_baselines3.common`)**
   - 包含强化学习通用组件：
     - `distributions`: 定义动作分布（如高斯、分类分布）。
     - `preprocessing`: 数据预处理工具（如图像归一化）。
     - `type_aliases`: 类型别名（如 `Schedule` 表示学习率调度）。
     - `utils`: 工具函数（如设备管理 `get_device`）。
     - `policies`: 策略基类（`BasePolicy`, `ActorCriticPolicy`）。

---

### **本地模块调用**
1. **`king_of_fighter.ppo.torch_layers`**
   - 自定义神经网络层：
     - `NatureCNN`: CNN特征提取器（仿DeepMind Nature论文结构）。
     - `BaseFeaturesExtractor`, `CombinedExtractor`: 特征提取器基类。
     - `MlpExtractor`: MLP网络用于策略和价值分支。

---

### **代码核心功能**
- **`ActorCriticCnnPolicy` 类**:
  - 继承自 `ActorCriticPolicy`，专为图像观测设计。
  - 使用 `NatureCNN` 作为默认特征提取器处理图像输入。
  - 通过 `MlpExtractor` 构建策略（Actor）和价值（Critic）网络。
  - 支持状态依赖探索（SDE）和多种动作分布（如高斯、分类）。

- **关键方法**:
  - `forward()`: 前向传播，输出动作、值估计和动作对数概率。
  - `evaluate_actions()`: 评估动作的价值和概率。
  - `predict_values()`: 预测状态价值。

---

### **依赖关系示例**
```python
# Stable Baselines3 组件
from stable_baselines3.common.distributions import DiagGaussianDistribution
from stable_baselines3.common.policies import ActorCriticPolicy

# 本地自定义层
from .torch_layers import NatureCNN, MlpExtractor
```

该代码通过结合Stable Baselines3的强化学习框架与自定义CNN模块，实现了适用于图像输入环境的Actor-Critic策略。

---

## king_of_fighter\ppo\dummy_vec_env.py

文件路径: `king_of_fighter\ppo\dummy_vec_env.py`

### AI分析说明



这份代码主要实现了强化学习中的向量化环境包装器`DummyVecEnv`，用于将多个强化学习环境包装成一个向量化环境，以便于批处理操作。以下是它调用的库及其作用：

1. **gymnasium**：创建和管理强化学习环境，代码中用作环境的基类。
2. **numpy**：处理数组和矩阵运算，用于存储和操作环境的状态、奖励等数据。
3. **stable_baselines3**：提供向量化环境的基类和工具，帮助实现高效的批处理操作。

此外，代码还使用了Python标准库中的`warnings`、`collections`、`copy`和`typing`模块，分别用于警告处理、有序字典、深度复制和类型注释。

---

## king_of_fighter\ppo\on_policy_algorithm.py

文件路径: `king_of_fighter\ppo\on_policy_algorithm.py`

### AI分析说明



该代码实现了一个基于PPO（Proximal Policy Optimization）算法的双玩家对战强化学习模型，主要调用了以下库：

1. **PyTorch (torch)**：
- 用于构建神经网络策略（ActorCriticPolicy）
- 实现张量计算和自动梯度
- 在GPU/CPU设备上进行数值运算

2. **Gymnasium**：
- 提供环境接口（GymEnv）
- 定义动作/观测空间（spaces.Box/spaces.Dict）
- 处理多环境并行（VecEnv）

3. **Stable Baselines3**：
- 继承BaseAlgorithm基类
- 使用RolloutBuffer/DictRolloutBuffer进行经验回放
- 通过ActorCriticPolicy实现策略-价值网络
- 利用安全均值计算（safe_mean）等工具函数

4. **NumPy**：
- 处理数组运算
- 实现动作裁剪等数值操作
- 记录训练统计数据

代码特点：
1. 双策略架构：包含policy_p1和policy_p2两个独立策略网络，分别对应两个玩家
2. 自适应训练：根据胜率动态切换训练对象（training_player变量）
3. 多样性奖励：通过action_memory记录动作多样性并计算奖励
4. 复合奖励机制：结合伤害奖励（damage_reward）和防御奖励（defense_reward）
5. 对抗训练：通过win_rate判断胜负关系，实现策略的对抗进化

典型应用场景：格斗游戏AI训练，支持双智能体在对抗环境中同步/交替学习攻防策略。

---

## king_of_fighter\ppo\ppo.py

文件路径: `king_of_fighter\ppo\ppo.py`

### AI分析说明



该代码实现了PPO（Proximal Policy Optimization）算法，主要用于强化学习训练。以下是调用的主要库及其作用：

---

### **第三方库**
1. **`numpy` (as np)**
   - 数值计算，处理数组和矩阵运算。

2. **`torch` (as th)**
   - PyTorch 深度学习框架，用于构建神经网络、自动求导和优化。

3. **`gymnasium.spaces`**
   - 定义强化学习环境的状态和动作空间（如 `Box`, `Discrete`）。

4. **`torch.nn.functional` (as F)**
   - PyTorch 的神经网络函数库，包含激活函数和损失函数（如 `F.mse_loss`）。

5. **`stable_baselines3` 的子模块**
   - `common.on_policy_algorithm`: 提供基于策略的算法基类 `OnPolicyAlgorithm`。
   - `common.policies`: 定义策略网络（如 `ActorCriticPolicy`）。
   - `common.type_aliases`: 类型别名（如 `GymEnv`, `Schedule`）。
   - `common.utils`: 工具函数（如 `get_schedule_fn` 调整学习率）。

---

### **本地模块**
1. **`.cnn_policy`**
   - 自定义的 CNN 策略 `ActorCriticCnnPolicy`，位于 `king_of_fighter/ppo` 目录下。

2. **`.on_policy_algorithm`**
   - 自定义的基类 `OnPolicyAlgorithm`，扩展自 `stable_baselines3` 的实现。

---

### **关键功能**
- **PPO 算法核心**：通过 `train_p1()` 和 `train_p2()` 分别训练两个策略（如双智能体对抗），使用 Clip 机制限制策略更新幅度。
- **优化目标**：结合策略损失（`policy_loss`）、值函数损失（`value_loss`）和熵正则项（`entropy_loss`）。
- **自适应学习率**：通过 `get_schedule_fn` 动态调整学习率和 Clip 范围。
- **梯度裁剪**：`th.nn.utils.clip_grad_norm_` 防止梯度爆炸。

---

代码通过继承 `OnPolicyAlgorithm` 并实现双策略训练逻辑，适用于需要双智能体交互的场景（如格斗游戏）。

---

## king_of_fighter\ppo\resnet_customer.py

文件路径: `king_of_fighter\ppo\resnet_customer.py`

### AI分析说明



这段代码主要使用了以下几个库：

1. **torchvision.models**：用于导入预训练的ResNet18模型。
2. **torch.nn**：用于构建神经网络模型，包括线性层和各种激活函数。
3. **torch**：用于张量操作和GPU加速。
4. **torch.nn.functional**：用于访问各种激活函数和层操作，如interpolate和relu。

代码定义了一个自定义的ResNet18模型，继承自nn.Module，并在其基础上添加了一个线性层。在前向传播过程中，使用了ResNet18的卷积层、批归一化层、激活函数和最大池化层，然后将特征图展平后通过线性层输出。

---

## king_of_fighter\ppo\resnet_policy.py

文件路径: `king_of_fighter\ppo\resnet_policy.py`

### AI分析说明



该代码定义了一个基于ResNet的Actor-Critic策略类，主要用于PPO等强化学习算法。以下是调用的主要库及作用说明：

---

### **调用的第三方库**
1. **`numpy` (np)**
   - 数值计算，处理数组数据。

2. **`torch` (th) 和 `torch.nn`**
   - PyTorch深度学习框架，用于构建神经网络（如全连接层、ResNet）。
   - 关键组件：`nn.Module`（网络基类）、`nn.Tanh`（激活函数）。

3. **`torchvision.models`**
   - 提供预训练模型（如ResNet），但代码中通过自定义模块`resnet18_customer`间接使用。

4. **`gymnasium.spaces`**
   - 定义强化学习的观测空间（`observation_space`）和动作空间（`action_space`）。

5. **`stable_baselines3.common` 子模块**
   - `distributions`：定义动作分布（如高斯、分类分布）。
   - `preprocessing`：数据预处理（如图像归一化）。
   - `type_aliases` 和 `utils`：工具函数（如设备管理、张量转换）。
   - `policies`：基础策略类（如`ActorCriticPolicy`的父类）。

---

### **调用的本地模块**
1. **`.resnet_customer.resnet18_customer`**
   - 自定义的ResNet-18模型，用作特征提取器（`features_extractor`）。

2. **`.torch_layers` 中的类**
   - `BaseFeaturesExtractor`（特征提取器基类）、`MlpExtractor`（MLP网络）等。

---

### **代码核心功能**
1. **策略架构**
   - 继承自`ActorCriticPolicy`，包含Actor（策略网络）和Critic（价值网络）。
   - 使用ResNet作为特征提取器（替换默认的Flatten/CNN提取器）。

2. **关键方法**
   - `forward()`: 前向传播，输出动作、价值估计和动作对数概率。
   - `evaluate_actions()`: 评估动作的价值和熵。
   - 支持状态依赖探索（SDE）和多种动作分布。

---

### **依赖关系示例**
```python
# 特征提取器使用自定义ResNet
self.features_extractor = resnet18_customer()

# 策略和价值网络构建
self.action_net = ...  # 基于latent_pi生成动作分布
self.value_net = nn.Linear(...)  # 输出价值估计
```

该代码通过结合ResNet的特征提取能力和强化学习策略，适用于需要处理图像输入的任务（如游戏AI）。

---

## king_of_fighter\ppo\torch_layers.py

文件路径: `king_of_fighter\ppo\torch_layers.py`

### AI分析说明



该代码调用了以下第三方库：

1. `gymnasium`：用于强化学习环境空间的定义（如`gym.Space`, `spaces.Box`, `spaces.Dict`），是OpenAI Gym的分支版本。
2. `torch`（PyTorch）：用于构建神经网络模块（如`nn.Module`, `nn.Conv2d`, `nn.Linear`）和张量操作。
3. `stable_baselines3.common`：包含三个子模块的调用：
   - `preprocessing`：提供`get_flattened_obs_dim`（计算展平观测维度）和`is_image_space`（判断是否为图像空间）。
   - `type_aliases`：定义`TensorDict`类型（张量字典）。
   - `utils`：提供`get_device`（自动获取PyTorch计算设备）。

代码核心功能：
1. 实现特征提取器基类（`BaseFeaturesExtractor`）及其子类：
   - `FlattenExtractor`：展平输入的特征提取器。
   - `NatureCNN`：基于DQN Nature论文的CNN结构，处理图像观测。
   - `CombinedExtractor`：组合处理字典观测空间（混合CNN和MLP）。

2. 工具函数：
   - `create_mlp`：动态构建多层感知机（MLP）。
   - `get_actor_critic_arch`：解析策略网络和价值网络的架构配置。

3. `MlpExtractor`类：构建分离的策略网络（Actor）和价值网络（Critic），支持自定义隐藏层结构。

---

