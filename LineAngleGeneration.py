import matplotlib.pyplot as plt
import numpy as np


def DrawFixation(stereoMode, axe: plt.Axes):
    offsetfix = 0
    len = 15
    xcenterL = ycenterL = xcenterR = ycenterR = xcenter = ycenter = 0

    if stereoMode == 0:
        # left eye
        axe.plot([xcenterL - len, xcenterL - len], [ycenterL - len - offsetfix, ycenterL + len - offsetfix], c='white')
        axe.plot([xcenterL + len, xcenterL + len], [ycenterL - len - offsetfix, ycenterL + len - offsetfix], c='white')
        axe.plot([xcenterL - len, xcenterL + len], [ycenterL - len - offsetfix, ycenterL - len - offsetfix], c='white')
        axe.plot([xcenterL - len, xcenterL + len], [ycenterL + len - offsetfix, ycenterL + len - offsetfix], c='white')

        # right eye
        axe.plot([xcenterR - len, xcenterR - len], [ycenterR - len - offsetfix, ycenterR + len - offsetfix], c='white')
        axe.plot([xcenterR + len, xcenterR + len], [ycenterR - len - offsetfix, ycenterR + len - offsetfix], c='white')
        axe.plot([xcenterR - len, xcenterR + len], [ycenterR - len - offsetfix, ycenterR - len - offsetfix], c='white')
        axe.plot([xcenterR - len, xcenterR + len], [ycenterR + len - offsetfix, ycenterR + len - offsetfix], c='white')

        # frontier
        axe.plot([xcenterR, xcenterR], [ycenterR - offsetfix + len, ycenterR + len * 2 - offsetfix], c='white')
        axe.plot([xcenterR + len, xcenterR + len * 2], [ycenterR - offsetfix, ycenterR - offsetfix], c='white')
        axe.plot([xcenterL, xcenterL], [ycenterL - offsetfix - len * 2, ycenterL - offsetfix - len], c='white')
        axe.plot([xcenterL - len * 2, xcenterL - len], [ycenterL - offsetfix, ycenterL - offsetfix], c='white')
    else:
        axe.plot([xcenter - len, xcenter - len], [ycenter - len - offsetfix, ycenter + len - offsetfix], c='white')
        axe.plot([xcenter + len, xcenter + len], [ycenter - len - offsetfix, ycenter + len - offsetfix], c='white')
        axe.plot([xcenter - len, xcenter + len], [ycenter - offsetfix - len, ycenter - offsetfix - len], c='white')
        axe.plot([xcenter - len, xcenter + len], [ycenter - offsetfix + len, ycenter - offsetfix + len], c='white')
        axe.plot([xcenter, xcenter], [ycenter - offsetfix - len * 2, ycenter - offsetfix - len], c='white')
        axe.plot([xcenter - len * 2, xcenter - len], [ycenter - offsetfix, ycenter - offsetfix], c='white')

        axe.plot([xcenter - len, xcenter - len], [ycenter - len - offsetfix, ycenter + len - offsetfix], c='white')
        axe.plot([xcenter + len, xcenter + len], [ycenter - len - offsetfix, ycenter + len - offsetfix], c='white')
        axe.plot([xcenter - len, xcenter + len], [ycenter - offsetfix - len, ycenter - offsetfix - len], c='white')
        axe.plot([xcenter - len, xcenter + len], [ycenter - offsetfix + len, ycenter - offsetfix + len], c='white')
        axe.plot([xcenter, xcenter], [ycenter - offsetfix + len, ycenter + len * 2 - offsetfix], c='white')
        axe.plot([xcenter + len, xcenter + len * 2], [ycenter - offsetfix, ycenter - offsetfix], c='white')


def DrawLineAngle(angleSize, stereoMode, axe) -> None:
    DrawFixation(stereoMode, axe)

    # black
    lineColor = [255, 255, 255]
    lineColor = np.array(lineColor) // 1000

    squareSize = 375 * 0.6
    Len = squareSize / 2

    xcenterL = ycenterL = xcenterR = ycenterR = xcenter = ycenter = 0

    if stereoMode == 0:
        XL_1 = xcenterL + np.sin(angleSize * np.pi / 360) * Len
        YL_1 = ycenterL - np.cos(angleSize * np.pi / 360) * Len

        XL_2 = xcenterL - np.sin(angleSize * np.pi / 360) * Len
        YL_2 = ycenterL - np.cos(angleSize * np.pi / 360) * Len

        XR_1 = xcenterR + np.sin(angleSize * np.pi / 360) * Len
        YR_1 = ycenterR - np.cos(angleSize * np.pi / 360) * Len

        XR_2 = xcenterR - np.sin(angleSize * np.pi / 360) * Len
        YR_2 = ycenterR - np.cos(angleSize * np.pi / 360) * Len

        axe.plot([XL_1, xcenterL], [YL_1, ycenterL], c='white')
        axe.plot([XL_2, xcenterL], [YL_2, ycenterL], c='white')
        axe.plot([XR_1, xcenterR], [YR_1, ycenterR], c='white')
        axe.plot([XR_2, xcenterR], [YR_2, ycenterR], c='white')
    else:
        XL_1 = xcenter + np.sin(angleSize * np.pi / 360) * Len
        YL_1 = ycenter - np.cos(angleSize * np.pi / 360) * Len

        XL_2 = xcenter - np.sin(angleSize * np.pi / 360) * Len
        YL_2 = ycenter - np.cos(angleSize * np.pi / 360) * Len

        XR_1 = xcenter + np.sin(angleSize * np.pi / 360) * Len
        YR_1 = ycenter - np.cos(angleSize * np.pi / 360) * Len

        XR_2 = xcenter - np.sin(angleSize * np.pi / 360) * Len
        YR_2 = ycenter - np.cos(angleSize * np.pi / 360) * Len

        axe.plot([XL_1, xcenter], [YL_1, ycenter], c='white')
        axe.plot([XL_2, xcenter], [YL_2, ycenter], c='white')
        axe.plot([XR_1, xcenter], [YR_1, ycenter], c='white')
        axe.plot([XR_2, xcenter], [YR_2, ycenter], c='white')


if __name__ == '__main__':
    num = 1
    angles = np.arange(90, 180, 10)

    for angle in angles:
        fig = plt.figure()  # type: plt.Figure
        ax = fig.add_subplot(111)  # type: plt.Axes
        # 禁用坐标轴与边框
        ax.axis("off")
        # figure画布默认宽高比 => 4 : 3
        plt.xlim(-200, 200)
        plt.ylim(-150, 150)
        # 更改画板背景为灰色
        fig.patch.set_facecolor("grey")

        DrawLineAngle(angle, 0, ax)
        plt.savefig("./Figures/LineAngleFigures/line_angle_figure_{}.jpg".format(num))
        plt.close(fig)
        num += 1
