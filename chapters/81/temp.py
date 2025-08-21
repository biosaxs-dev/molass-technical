"""

"""

import sys
sys.path.insert(0, r"D:\GitHub\molass-library")
from molass import get_version
assert get_version() >= '0.4.0', "This tutorial requires molass version 0.4.0 or higher."

import matplotlib.pylab as plt
from molass.SEC.ColumnSimulation import get_animation

save_animation = False
blit = save_animation

anim = get_animation(num_frames=600, interval=100, seed=1234, close_plot=False, return_init=False, blit=blit, use_tqdm=False)

plt.show()

if save_animation:
    to_mp4 = True
    if to_mp4:
        # Save the animation as an MP4 file
        anim.save("sec-saxs.mp4", writer="ffmpeg", fps=30)
    else:
        # Save the animation as an HTML file
        anim.save("sec-saxs.gif")