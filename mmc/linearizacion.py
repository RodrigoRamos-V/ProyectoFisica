from mmc import MMC

t = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
Y = [0.000000, 0.313, 0.627, 0.942, 1.256, 1.571]

mmc = MMC(x=t, y=Y)

print(mmc.A, mmc.B, mmc.A_err, mmc.B_err)
