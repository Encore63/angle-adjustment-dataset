import matplotlib.pyplot as plt
import numpy as np


def DrawRDS(MaxDiffPixel, axe_left: plt.Axes, axe_right: plt.Axes) -> None:
    iDotSize = 6
    iDotCount: int = 1000
    dots = np.zeros([3, iDotCount])  # type: np.ndarray
    # width, height = (1920, 1080)
    # MM_Per_Pixel_W = iMonitorWidth / width
    # MM_Per_Pixel_H = iMonitorHeight / height
    a = 375 * 0.3
    xmax = a
    ymax = xmax
    MinDisparityPixel = 0

    # color = list()
    # zero = list()

    color = np.zeros([3, iDotCount])
    for i in range(0, iDotCount):
        if i % 2 == 0:
            color[0, i] = 255
            color[1, i] = 0
            color[2, i] = 0
        else:
            color[0, i] = 0
            color[1, i] = 0
            color[2, i] = 255

    zero = np.zeros([1, iDotCount])

    dots[0, :] = 2 * xmax * np.random.random(iDotCount) - xmax
    dots[1, :] = 2 * ymax * np.random.random(iDotCount) - ymax
    dots[2, :] = (np.abs(dots[1, :]) / xmax) * (MaxDiffPixel - MinDisparityPixel)

    xy_1 = dots[0:2, :] - np.append(dots, values=zero, axis=0)[2:, :]
    xy_2 = dots[0:2, :] + np.append(dots, values=zero, axis=0)[2:, :]

    color = color.T / 1000

    axe_left.scatter(xy_1[1, :], xy_1[0, :], c='white', s=iDotSize)
    axe_right.scatter(xy_2[1, :], xy_2[0, :], c='black', s=iDotSize)


if __name__ == '__main__':
    num = 1
    pixels = np.arange(5.0, 10.0, 0.5)

    for pixel in pixels:
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

        DrawRDS(pixel, ax_left, ax_right)
        fig_left.savefig("./Figures/BinocularRDSFigures/scatter_dots_figure_left_{}.jpg".format(num))
        fig_right.savefig("./Figures/BinocularRDSFigures/scatter_dots_figure_right_{}.jpg".format(num))

        plt.close(fig_left)
        plt.close(fig_right)
        num += 1
