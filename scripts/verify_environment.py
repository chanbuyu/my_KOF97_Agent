def verify_environment():
    """验证环境安装是否正确"""
    try:
        # 验证PyTorch安装
        import torch
        print(f"PyTorch版本: {torch.__version__}")
        print(f"CUDA是否可用: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"当前CUDA版本: {torch.version.cuda}")
            print(f"当前使用的GPU: {torch.cuda.get_device_name(0)}")

        # 验证其他依赖包
        import gymnasium as gym
        print("\nGymnasium导入成功")
        
        import stable_baselines3
        print("Stable-baselines3导入成功")
        
        import MAMEToolkit
        print("MAMEToolkit导入成功")

        print("\n所有依赖包验证完成！环境搭建成功！")
        return True

    except ImportError as e:
        print(f"\n环境验证失败: {str(e)}")
        return False

if __name__ == "__main__":
    verify_environment() 