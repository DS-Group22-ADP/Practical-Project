def setup_gridspec__one_main__two_side_subplots(plt):
    # start with a square Figure
    fig = plt.figure(figsize=(20, 20))
    fig.tight_layout(pad=2.0)

    fig.suptitle("Average Height Percentage vs Ground Floor Type Distinguished by Other Floor Type (color) and Quantity of values (size)")
    gs = fig.add_gridspec(2, 2,  width_ratios=(7,4), height_ratios=(3,7),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.15, hspace=0.15)
    ax_0_0 = fig.add_subplot(gs[1,0])

    ax1_histx = fig.add_subplot(gs[0, 0], sharex=ax_0_0)
    ax1_histy = fig.add_subplot(gs[1, 1], sharey=ax_0_0)

    return {"gridspec": gs, "ax": ax_0_0, "axx": ax1_histx, "axy": ax1_histy, "fig": fig}



