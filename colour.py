import numpy as np
import matplotlib.pyplot as plt
import textwrap
 
class Colour:
    def __init__(self, name, rgb, format="decimal"):
        self.name = name
        if format == "decimal":
            self.vector = list(np.array(rgb) / 255.0)  # Normalize the rgb values to [0,1]
        if format == "normalised":
            self.vector = rgb
        if format == "hex":
            rgb = [int(rgb[i:i+2], 16) for i in (0, 2, 4)]
            self.vector = list(np.array(rgb) / 255.0)

    def __repr__(self):
        return f"('{self.name}', {self.vector})"
    
    def as_hex(self):
        return ''.join(['{:02x}'.format(int(c * 255)) for c in self.vector])


def plot_colours(query_colour, similar_colours):
    fig, axs = plt.subplots(6, 1, figsize=(5, 18))

    # Set the title
    title_text = f'Colours Similar to {query_colour.name} ({query_colour.as_hex()})'
    title_text = textwrap.fill(title_text, width=30)  # Wrap the text
    fig.text(0.5, 0.95, title_text, ha='center', va='top', fontsize=16, wrap=True)

    # Plot the query colour
    axs[0].imshow([[query_colour.vector]])
    axs[0].axis('off')
    axs[0].set_title(f'Query:\n{query_colour.name}\n{query_colour.as_hex()}', fontsize=12, rotation='horizontal')

    # Plot the similar colours
    for ax, colour in zip(axs[1:], similar_colours):
        this_colour = Colour(colour.id, colour.values, format="normalised")
        ax.imshow([[this_colour.vector]])
        ax.axis('off')
        score_percent = round(colour.score*100, 2)
        ax.set_title(f'{this_colour.name}\n{this_colour.as_hex()}\n{score_percent}% similar', fontsize=12, rotation='horizontal')

    # Adjust the vertical spacing
    fig.subplots_adjust(hspace=1)

    plt.tight_layout()
    # Save the plot as a PNG image
    plt.savefig(f'output/{query_colour.name}_similar_colours.png', bbox_inches='tight')

