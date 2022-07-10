import matplotlib.pyplot as plt
import numpy as np


def DrawPerspective(theta, axe: plt.Axes) -> None:
    a = b = 375 * 0.3
    numOfLines = 5

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
    #   white
    cor1 = np.array([0, 0, 0])
    #   black
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

    VLines = np.array([VLineX, VLineY])

    HLineX = np.array([])
    HLineY = np.array([])

    # Horizontal Lines
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

    HLines = np.array([HLineX, HLineY])

    vx: np.ndarray = VLines[0].reshape(VLines[0].size // 2, 2)
    vy: np.ndarray = VLines[1].reshape(VLines[1].size // 2, 2)

    hx: np.ndarray = HLines[0].reshape(HLines[0].size // 2, 2)
    hy: np.ndarray = HLines[1].reshape(HLines[1].size // 2, 2)

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

    for i in range(0, len(vx)):
        axe.plot(vx[i], vy[i], color=vc[i])
    for i in range(len(hy)):
        axe.plot(hx[i], hy[i], color=hc[i])


if __name__ == '__main__':
    num = 1
    plt.xlim(-16, 16)
    index = np.arange(1.0, 2.0, 0.1)

    for idx in index:
        fig: plt.Figure = plt.figure()
        ax: plt.Axes = fig.add_subplot(111)
        # 禁用坐标轴与边框
        ax.axis("off")
        # 更改画板背景为灰色
        fig.patch.set_facecolor("grey")
        DrawPerspective(idx, ax)
        plt.savefig("./Figures/PerspectiveFigures/perspective_figure_{}.jpg".format(num))
        plt.close(fig)
        num += 1
