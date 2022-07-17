import os
import re

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scio

import BinocularRDSGeneration
import LineAngleGeneration
import LineDisparityGeneration
import PerspectiveGeneration


class DataSetFigures(object):
    __angle_size = 0
    __theta = 0
    __max_diff_pixel = 0

    def __init__(self,angle_size, theta, max_diff_pixel) -> None:
        self.__angle_size = angle_size
        self.__theta = theta
        self.__max_diff_pixel = max_diff_pixel

    def GenerateLineAngleDataSet(self, address: str, name: str, index: int) -> None:
        fig = plt.figure()  # type: plt.Figure
        ax = fig.add_subplot(111)  # type: plt.Axes
        # 禁用坐标轴与边框
        ax.axis("off")
        # figure画布默认宽高比 => 4 : 3
        plt.xlim(-200, 200)
        plt.ylim(-150, 150)
        # 更改画板背景为灰色
        fig.patch.set_facecolor("grey")

        LineAngleGeneration.DrawLineAngle(self.__angle_size, 0, ax)
        fig.savefig(address + "/angle_{0}_{1}.jpg".format(name, index))

        plt.close(fig)

    def GeneratePerspectiveDataSet(self, address: str, name: str, index: int) -> None:
        fig: plt.Figure = plt.figure()
        ax: plt.Axes = fig.add_subplot(111)
        # 禁用坐标轴与边框
        ax.axis("off")
        # 更改画板背景为灰色
        fig.patch.set_facecolor("grey")

        PerspectiveGeneration.DrawPerspective(self.__theta, ax)
        fig.savefig(address + "/perspective_{0}_{1}.jpg".format(name, index))

        plt.close(fig)

    def GenerateLineDisparityDataSet(self, address: str, name: str, index: int) -> None:
        fig_left: plt.Figure = plt.figure()
        ax_left: plt.Axes = fig_left.add_subplot(111)
        # 禁用坐标轴与边框
        ax_left.axis("off")
        # 更改画板背景为灰色
        fig_left.patch.set_facecolor("grey")

        fig_right: plt.Figure = plt.figure()
        ax_right: plt.Axes = fig_right.add_subplot(111)
        # 禁用坐标轴与边框
        ax_right.axis("off")
        # 更改画板背景为灰色
        fig_right.patch.set_facecolor("grey")

        LineDisparityGeneration.DrawLineDisparity(self.__max_diff_pixel, ax_left, ax_right)
        fig_left.savefig(address + "/disparity_left_{0}_{1}.jpg".format(name, index))
        fig_right.savefig(address + "/disparity_right_{0}_{1}.jpg".format(name, index))

        plt.close(fig_left)
        plt.close(fig_right)

    def GenerateRDSDataSet(self, address: str, name: str, index: int) -> None:
        # left figure
        fig_left = plt.figure()  # type: plt.Figure
        ax_left = fig_left.add_subplot(111)  # type: plt.Axes
        ax_left.axis("off")
        fig_left.patch.set_facecolor("grey")

        # right figure
        fig_right = plt.figure()  # type: plt.Figure
        ax_right = fig_right.add_subplot(111)  # type: plt.Axes
        ax_right.axis("off")
        fig_right.patch.set_facecolor("grey")

        BinocularRDSGeneration.DrawRDS(self.__max_diff_pixel, ax_left, ax_right)
        fig_left.savefig(address + "/rds_left_{0}_{1}.jpg".format(name, index))
        fig_right.savefig(address + "/rds_right_{0}_{1}.jpg".format(name, index))

        plt.close(fig_left)
        plt.close(fig_right)


def GetName(file_name: str) -> str:
    regex = re.compile(r'AT_[\S]+_')
    return re.match(regex, file_name).group()[3: -3]


def LoadMatFile(filename: str) -> dict:
    file = os.path.join('./Data', filename)
    return scio.loadmat(file)


def FigureClassify(data_addr: str) -> None:
    data = os.listdir(data_addr)
    for file_name in data:
        rds_path = "./Figures/BinocularRDSFigures"
        if not os.path.exists(rds_path):
            os.makedirs(rds_path)
        line_angle_path = "./Figures/LineAngleFigures"
        if not os.path.exists(line_angle_path):
            os.makedirs(line_angle_path)
        line_disparity_path = "./Figures/LineDisparityFigures"
        if not os.path.exists(line_disparity_path):
            os.makedirs(line_disparity_path)
        perspective_path = "./Figures/PerspectiveFigures"
        if not os.path.exists(perspective_path):
            os.makedirs(perspective_path)

        angle_sizes: np.ndarray = LoadMatFile(file_name).get('trialList')[:, :1]
        max_diff_pixels: np.ndarray = LoadMatFile(file_name).get('MaxDiffList')[0]
        thetas: np.ndarray = LoadMatFile(file_name).get('thetaList')[0]
        length = (max_diff_pixels.size + thetas.size) // 2
        name = GetName(file_name)

        rds_path = "".join(rds_path + '/' + name)
        line_angle_path = "".join(line_angle_path + '/' + name)
        line_disparity_path = "".join(line_disparity_path + '/' + name)
        perspective_path = "".join(perspective_path + '/' + name)
        if not os.path.exists(rds_path):
            os.makedirs(rds_path)
        else:
            rds_path = None
        if not os.path.exists(line_angle_path):
            os.makedirs(line_angle_path)
        else:
            line_angle_path = None
        if not os.path.exists(line_disparity_path):
            os.makedirs(line_disparity_path)
        else:
            line_disparity_path = None
        if not os.path.exists(perspective_path):
            os.makedirs(perspective_path)
        else:
            perspective_path = None

        for index in range(length):
            theta = thetas[index]
            max_diff_pixel = max_diff_pixels[index]
            angle_size = angle_sizes[index]

            figures: DataSetFigures = DataSetFigures(angle_size, theta, max_diff_pixel)
            if line_angle_path is not None:
                figures.GenerateLineAngleDataSet(line_angle_path, name, index)
            if rds_path is not None:
                figures.GenerateRDSDataSet(rds_path, name, index)
            if perspective_path is not None:
                figures.GeneratePerspectiveDataSet(perspective_path, name, index)
            if line_disparity_path is not None:
                figures.GenerateLineDisparityDataSet(line_disparity_path, name, index)


if __name__ == '__main__':
    FigureClassify("./Data")
