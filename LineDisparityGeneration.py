import matplotlib.pyplot as plt
import numpy as np


def DrawLineDisparity(MaxDiffPixel, axe_left: plt.Axes, axe_right: plt.Axes) -> None:
    numOfLines = 5
    theta = 1
    a = 375 * 0.3
    b = a

    # Vertical Lines
    X = []
    Y = []
    deltaX = (2 * a + 1) / (numOfLines - 1)
    deltaY = (2 * b + 1) / (numOfLines - 1)

    # width = 3
    # Smooth = 1

    for i in range(1, numOfLines + 1):
        X.append(np.floor(-a + (i - 1) * deltaX))
        Y.append(np.floor(-a + (i - 1) * deltaY))

    X = np.array(X)
    Y = np.array(Y)

    Y0 = Y
    Y2 = Y
    Y1 = Y

    VLineX: np.ndarray = np.array([])
    VLineY: np.ndarray = np.array([])

    VLineColor = np.array([])
    HLineColor = np.array([])
    #   white color
    cor1 = np.array([0, 0, 0])
    #   black color
    cor2 = np.array([255, 255, 255])

    LineMinPixel = 20
    LineMaxPixel = 30

    for i in range(0, numOfLines):
        if X[i] <= 0:
            beta = (X[i] - (-a)) / a
            delta: float = (b * theta - b) * beta
            ymin: float = -b - delta
            ymax: float = b + delta
        else:
            beta = (a - X[i]) / a
            delta: float = (b * theta - b) * beta
            ymin: float = -b - delta
            ymax: float = b + delta

        y = ymin
        isCor1 = 1

        while y < ymax:
            NextLength = LineMinPixel + (LineMaxPixel - LineMinPixel) * np.random.rand()
            YEnd = y + NextLength
            if YEnd > ymax:
                YEnd = ymax
            VLineY = np.append(VLineY, [y, YEnd], axis=0)
            VLineX = np.append(VLineX, [X[i], X[i]], axis=0)
            y: float = YEnd
            if isCor1 == 1:
                VLineColor = np.append(VLineColor, cor1, axis=0)
                VLineColor = np.append(VLineColor, cor1, axis=0)
                isCor1 = 0
            else:
                VLineColor = np.append(VLineColor, cor2, axis=0)
                VLineColor = np.append(VLineColor, cor2, axis=0)
                isCor1 = 1

    VLineXLeftEye = VLineX - (np.abs(VLineX) / a) * MaxDiffPixel
    VLineXRightEye = VLineX + (np.abs(VLineX) / a) * MaxDiffPixel
    VLinesLeft = np.array([VLineXLeftEye, VLineY])
    VLinesRight = np.array([VLineXRightEye, VLineY])

    # Horizontal Lines
    HLineX = np.array([])
    HLineY = np.array([])

    for i in range(0, numOfLines):
        xmin = -a
        ymin = Y0[i]

        k = (Y1[i] * theta - Y0[i]) / a
        c = Y1[i] * theta
        isCor1 = 1

        while xmin < 0:
            NextLength = LineMinPixel + (LineMaxPixel - LineMinPixel) * np.random.rand()
            xend = xmin + NextLength
            if xend > 0:
                xend = 0
            HLineX = np.append(HLineX, [xmin, xend], axis=0)
            yend = k * xend + c
            HLineY = np.append(HLineY, [ymin, yend], axis=0)
            xmin = xend
            ymin = yend
            if isCor1 == 1:
                HLineColor = np.append(HLineColor, cor1, axis=0)
                HLineColor = np.append(HLineColor, cor1, axis=0)
                isCor1 = 0
            else:
                HLineColor = np.append(HLineColor, cor2, axis=0)
                HLineColor = np.append(HLineColor, cor2, axis=0)
                isCor1 = 1

        xmin = 0
        ymin = Y1[i] * theta

        k = (Y2[i] - Y1[i] * theta) / a
        c = Y1[i] * theta
        isCor1 = 1

        while xmin < a:
            NextLength = LineMinPixel + (LineMaxPixel - LineMinPixel) * np.random.rand()
            xend = xmin + NextLength
            if xend > a:
                xend = a
            HLineX = np.append(HLineX, [xmin, xend], axis=0)
            yend = k * xend + c
            HLineY = np.append(HLineY, [ymin, yend], axis=0)
            ymin = yend
            xmin = xend
            if isCor1 == 1:
                HLineColor = np.append(HLineColor, cor1, axis=0)
                HLineColor = np.append(HLineColor, cor1, axis=0)
                isCor1 = 0
            else:
                HLineColor = np.append(HLineColor, cor2, axis=0)
                HLineColor = np.append(HLineColor, cor2, axis=0)
                isCor1 = 1

    HLineXLeftEye = HLineX - (np.abs(HLineX) / a) * MaxDiffPixel
    HLineXRightEye = HLineX + (np.abs(HLineX) / a) * MaxDiffPixel
    HLinesLeftEye = np.array([HLineXLeftEye, HLineY])
    HLinesRightEye = np.array([HLineXRightEye, HLineY])

    VLineColor = np.reshape(VLineColor[::], (len(VLineColor[::]) // 3, 3))
    HLineColor = np.reshape(HLineColor[::2], (len(HLineColor[::2]) // 3, 3))

    hc = []
    vc = []
    for color in HLineColor:
        if color.tolist() == [0, 0, 0]:
            hc.append('white')
        elif color.tolist() == [255, 255, 255]:
            hc.append('black')

    for color in VLineColor:
        if color.tolist() == [0, 0, 0]:
            vc.append('white')
        elif color.tolist() == [255, 255, 255]:
            vc.append('black')

    vlx: np.ndarray = VLinesLeft[0].reshape(VLinesLeft[0].size // 2, 2)
    vly: np.ndarray = VLinesLeft[1].reshape(VLinesLeft[1].size // 2, 2)
    hlx: np.ndarray = HLinesLeftEye[0].reshape(HLinesLeftEye[0].size // 2, 2)
    hly: np.ndarray = HLinesLeftEye[1].reshape(HLinesLeftEye[1].size // 2, 2)

    vrx: np.ndarray = VLinesRight[0].reshape(VLinesRight[0].size // 2, 2)
    vry: np.ndarray = VLinesRight[1].reshape(VLinesRight[1].size // 2, 2)
    hrx: np.ndarray = HLinesRightEye[0].reshape(HLinesRightEye[0].size // 2, 2)
    hry: np.ndarray = HLinesRightEye[1].reshape(HLinesRightEye[1].size // 2, 2)

    # Draw Left Figure
    for i in range(len(vlx)):
        axe_left.plot(vlx[i], vly[i], color=vc[i])
    for i in range(len(hly)):
        axe_left.plot(hlx[i], hly[i], color=hc[i])

    # Draw Right Figure
    for i in range(len(vrx)):
        axe_right.plot(vrx[i], vry[i], color=vc[i])
    for i in range(len(hry)):
        axe_right.plot(hrx[i], hry[i], color=hc[i])


if __name__ == '__main__':
    num = 1
    plt.xlim(-16, 16)
    pixels = np.arange(5.0, 10.0, 0.5)

    for pixel in pixels:
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

        DrawLineDisparity(pixel, ax_left, ax_right)
        fig_left.savefig("./Figures/LineDisparityFigures/line_disparity_figure_left_{}.jpg".format(num))
        fig_right.savefig("./Figures/LineDisparityFigures/line_disparity_figure_right_{}.jpg".format(num))

        plt.close(fig_left)
        plt.close(fig_right)
        num += 1
