# 导入所需的模块
from configobj import ConfigObj  # 用于读取配置文件
import numpy as np  # 用于处理数组和数值运算


# 定义一个读取配置文件的函数
def config_reader():
    """
    该函数从配置文件 'config' 中读取模型的参数和相关配置。
    返回：
    - param: 全局参数（如 GPU 设置、分辨率范围等）
    - model: 与模型结构相关的参数（如输入图像大小、步幅等）
    """
    # 加载配置文件，配置文件名为 'config'
    config = ConfigObj('config')

    # 从配置文件中读取 'param' 参数块
    param = config['param']
    print(param)  # 输出读取的参数，方便调试

    # 读取全局参数中的模型编号（modelID）
    model_id = param['modelID']

    # 根据模型编号从配置文件中获取相应的模型配置
    model = config['models'][model_id]

    # 将配置文件中以字符串形式存储的参数转换为相应的数据类型
    model['boxsize'] = int(model['boxsize'])  # 输入图像的尺寸
    model['stride'] = int(model['stride'])  # 模型的步幅
    model['padValue'] = int(model['padValue'])  # 用于填充图像的像素值

    # 将 'param' 参数块中部分值也进行类型转换
    param['octave'] = int(param['octave'])  # 金字塔尺度的数量
    param['use_gpu'] = int(param['use_gpu'])  # 是否使用 GPU（1 表示使用）
    param['starting_range'] = float(param['starting_range'])  # 图像缩放的起始范围
    param['ending_range'] = float(param['ending_range'])  # 图像缩放的结束范围

    # 将 'scale_search' 转换为浮点数列表，用于多尺度搜索
    param['scale_search'] = map(float, param['scale_search'])

    # 将阈值参数转换为浮点数，用于模型的关键点检测
    param['thre1'] = float(param['thre1'])  # 第一类阈值
    param['thre2'] = float(param['thre2'])  # 第二类阈值
    param['thre3'] = float(param['thre3'])  # 第三类阈值

    # 其他参数转换为整数或浮点数
    param['mid_num'] = int(param['mid_num'])  # 中间处理层的数量
    param['min_num'] = int(param['min_num'])  # 最小检测数量
    param['crop_ratio'] = float(param['crop_ratio'])  # 图像裁剪比例
    param['bbox_ratio'] = float(param['bbox_ratio'])  # 边界框比例
    param['GPUdeviceNumber'] = int(param['GPUdeviceNumber'])  # 使用的 GPU 编号

    # 返回解析后的参数和模型配置
    return param, model


# 如果直接运行该脚本（而不是作为模块导入）
if __name__ == "__main__":
    # 调用 config_reader 函数，读取并打印配置
    config_reader()
