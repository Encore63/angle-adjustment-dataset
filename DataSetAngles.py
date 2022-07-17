import os

from DataSetFigures import DataSetFigures
from DataSetFigures import GetName
from DataSetFigures import LoadMatFile


def AngleClassify(data_addr: str):
    root_path = "./Angles"
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    file_names = os.listdir(data_addr)

    for file_name in file_names:
        data = LoadMatFile(file_name)
        name = GetName(file_name)
        for index in range(data.get('trialList')[:, :1].size):
            angle_size = data.get('trialList')[:, :1].tolist()[index][0]
            angle_path = "".join(root_path + "/" + str(angle_size))
            if not os.path.exists(angle_path):
                os.makedirs(angle_path)
            rds_path = "".join(angle_path + "/BinocularRDSFigures/" + name)
            if not os.path.exists(rds_path):
                os.makedirs(rds_path)
            else:
                rds_path = None
            line_angle_path = "".join(angle_path + "/LineAngleFigures/" + name)
            if not os.path.exists(line_angle_path):
                os.makedirs(line_angle_path)
            else:
                line_angle_path = None
            line_disparity_path = "".join(angle_path + "/LineDisparityFigures/" + name)
            if not os.path.exists(line_disparity_path):
                os.makedirs(line_disparity_path)
            else:
                line_disparity_path = None
            perspective_path = "".join(angle_path + "/PerspectiveFigures/" + name)
            if not os.path.exists(perspective_path):
                os.makedirs(perspective_path)
            else:
                perspective_path = None

            max_diff_pixel = LoadMatFile(file_name).get('MaxDiffList')[0].tolist()[index]
            theta = LoadMatFile(file_name).get('thetaList')[0].tolist()[index]

            figures: DataSetFigures = DataSetFigures(angle_size, theta, max_diff_pixel)
            if line_angle_path is not None:
                figures.GenerateLineAngleDataSet(line_angle_path, name, index)
            if rds_path is not None:
                figures.GenerateRDSDataSet(rds_path, name, index)
            if line_disparity_path is not None:
                figures.GenerateLineDisparityDataSet(line_disparity_path, name, index)
            if perspective_path is not None:
                figures.GeneratePerspectiveDataSet(perspective_path, name, index)


if __name__ == '__main__':
    AngleClassify("./Data")
