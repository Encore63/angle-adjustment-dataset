# Angle Adjust 数据集 
简介：本程序用于生成angle adjust的相关数据集

## 使用说明：  
1. LineAngleGeneration, PerspectiveFeneration, LineDisparityGeneration, RDSGeneration, BinocularRDSGeneration用于生成与程序名称相对应的图片文件, 其中RDSGeneration用于生成完整的、由红色与蓝色构成的散点图, 而BinocularRDSGeneration则用于生成左右成对的、由黑白两色构成的散点图。
2. DataSetFigures用于生成以图片类型和人名为分类依据的数据集，DataSetAngles用于生成以角度、图片类型和人民为分类依据的数据集。分别对应DataSetFigures中的FigureClassify(data_addr: str)函数和DataSetAngles中的AngleClassify(data_addr: str)函数，其中的data_addr参数值指实验数据(.mat)的路径
