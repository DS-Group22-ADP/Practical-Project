def setup_gridspec__one_main__two_side_subplots(plt):
    # start with a square Figure
    fig = plt.figure(figsize=(20, 20))
    fig.tight_layout(pad=2.0)

    gs = fig.add_gridspec(2, 2,  width_ratios=(7,4), height_ratios=(3,7),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.15, hspace=0.15)
    ax_0_0 = fig.add_subplot(gs[1,0])

    ax1_histx = fig.add_subplot(gs[0, 0], sharex=ax_0_0)
    ax1_histy = fig.add_subplot(gs[1, 1], sharey=ax_0_0)

    return {"gridspec": gs, "ax": ax_0_0, "axx": ax1_histx, "axy": ax1_histy, "fig": fig}

def setup_gridspec__four_main__two_side_subplots(plt):
    # start with a square Figure
    fig = plt.figure(figsize=(20, 20))
    fig.tight_layout(pad=2.0)

    gs = fig.add_gridspec(4, 4,  width_ratios=(7,4,7,4), height_ratios=(3,7,3,7),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.15, hspace=0.15)
    ax_0_0 = fig.add_subplot(gs[1,0])
    ax_0_1 = fig.add_subplot(gs[1,2])
    ax_1_0 = fig.add_subplot(gs[3,0])
    ax_1_1 = fig.add_subplot(gs[3,2])

    ax1_histx = fig.add_subplot(gs[0, 0], sharex=ax_0_0)
    ax1_histy = fig.add_subplot(gs[1, 1], sharey=ax_0_0)

    ax2_histx = fig.add_subplot(gs[0, 2], sharex=ax_0_1)
    ax2_histy = fig.add_subplot(gs[1, 3], sharey=ax_0_1)

    ax3_histx = fig.add_subplot(gs[2, 0], sharex=ax_1_0)
    ax3_histy = fig.add_subplot(gs[3, 1], sharey=ax_1_0)

    ax4_histx = fig.add_subplot(gs[2, 2], sharex=ax_1_1)
    ax4_histy = fig.add_subplot(gs[3, 3], sharey=ax_1_1)

    return {"gridspec": gs, "ax": (ax1,ax2), "axx": (ax1_histx, ax2_histx, ax3_histx, ax4_histx), 
            "axy": (ax1_histy, ax2_histy, ax3_histy, ax4_histy), "fig": fig}

