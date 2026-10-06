import matplotlib.pyplot as plt

def plot_spectrum(wavelength, absorption_dict, scattering_dict, extinction_dict, normalized_extinction_dict):

    fig, axes = plt.subplots(2, 2, figsize=(14,6), sharex=True)
    axes = axes.flatten()
    dicts = [
        absorption_dict,
        scattering_dict,
        extinction_dict,
        normalized_extinction_dict
    ]

    titles = [
        "Absorption Cross-Section",
        "Scattering Cross-Section",
        "Total Extinction Cross-Section",
        "Normalized Extinction"
    ]

    for i, data_dict in enumerate(dicts):

        ax = axes[i]

        for radius, data in data_dict.items():

            label = f"R={radius}nm"

            ax.plot(
                wavelength,
                data,
                linewidth=2,
                label=label
            )

        ax.set_title(titles[i], fontsize=14)
        ax.set_xlabel("Wavelength (nm)", fontsize=12)
        ax.set_ylabel("Cross Section (m$^2$)", fontsize=12)
        ax.set_xlim(300, 1200)
        ax.grid(True, linestyle="--", alpha=0.6)
        ax.legend(fontsize=9)

    plt.tight_layout()
    plt.show()