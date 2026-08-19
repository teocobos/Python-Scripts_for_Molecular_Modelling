from matplotlib import pylab as plt
import numpy as np

def gaussian(x, mu, sig):
    pref = 1 / (sig * (np.pi * 2) ** 0.05)
    return pref * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

# Safely opening the input file using a context manager
with open("tddft_silicon.log") as input_data:
    xval = []
    yval = []
    for lines in input_data:
        line_words = lines.split()
        if len(line_words) == 7:
            if line_words[0] == "TDDFPT|":
                xval.append(float(line_words[2]))
                yval.append(float(line_words[6]))

condition = "passed"
counter = len(xval)
while condition == "passed":
    counter = counter - 1
    if xval[counter - 1] > xval[counter]:
        condition = "failed"

final_xval = []
final_yval = []
xmin = 0
xmax = xval[len(xval) - 1]
for i in range(1000):
    x_value = xmin + (float(i) * (xmax - xmin)) / 1000.0
    y_value = 0
    for j in range(len(yval)):
        y_value += yval[j] * gaussian(x_value, xval[j], 0.05)
    final_yval.append(y_value)
    final_xval.append(x_value)

# Enhanced Plotting Section
plt.figure(figsize=(8, 6), dpi=300)  # Increase figure size and resolution for publication

# Plot the data
plt.plot(final_xval, final_yval, color='darkgreen', linewidth=2, label="Absorption Spectrum")

# Add gridlines and adjust grid style
plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Label axes with improved formatting
plt.xlabel('Excitation Energy (eV)', fontsize=14, fontweight='bold')
plt.ylabel('Absorbance (Arbitrary Units)', fontsize=14, fontweight='bold')

# Add axis ticks with proper scaling
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Set axis limits for clarity
plt.xlim([0, 8.3])
plt.ylim([0, 0.31])

# Add a legend
plt.legend(fontsize=12, loc='upper right', frameon=False)

# Optional: Add a title
# plt.title('Optical Absorption Spectrum', fontsize=16, fontweight='bold')

# Save the plot as a high-resolution PNG image
plt.tight_layout()  # Ensures no clipping of labels
plt.savefig('optical_plot_publication.png', format='png', dpi=300)
print("Plot saved as optical_plot_publication.png")
