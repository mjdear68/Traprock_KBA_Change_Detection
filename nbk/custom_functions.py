def remove_labels_ticks(ax):
    '''
    Remove axis labels and ticks from subplots.
    '''
    ax.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False)
    ax.set_xlabel('')
    ax.set_ylabel('')