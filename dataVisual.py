import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 100  
plt.rcParams['savefig.dpi'] = 300 
plt.rcParams['lines.linewidth'] = 2.5 
plt.rcParams['lines.markersize'] = 7  
plt.rcParams['font.family'] = 'sans-serif'


# # FID（close/lesion/full）
# close = np.array([
#     181.82, 211.46, 212.22, 172.63, 204.77,
#     210.79, 61.77, 90.14, 191.06, 195.77,
#     191.57, 190.02, 151.35, 177.85, 192.50,
#     227.37, 204.98, 182.15, 180.98, 220.06,
# ])
# lesion = np.array([
#     162.54, 218.44, 188.63, 154.34, 173.00,
#     208.55, 147.68, 140.95, 177.88, 184.75,
#     174.70, 181.59, 177.83, 172.06, 171.72,
#     208.10, 182.07, 160.94, 153.90, 187.43,
# ])
# full = np.array([
#     158.72, 164.39, 172.98, 136.58, 156.93,
#     173.60, 134.12, 128.51, 159.07, 155.49,
#     177.30, 160.41, 155.53, 160.56, 157.27,
#     158.63, 273.91, 156.93, 144.38, 157.66,
# ])

#  LPIPS
# close = np.array([
#     0.2678, 0.3574, 0.4614, 0.2163, 0.3123,
#     0.3025, 0.0951, 0.1585, 0.3016, 0.3047,
#     0.2922, 0.2888, 0.2602, 0.2827, 0.2801,
#     0.3575, 0.3182, 0.3783, 0.2797, 0.3626,
# ])

# lesion = np.array([
#     0.2778, 0.5116, 0.4583, 0.2250, 0.2781,
#     0.3552, 0.2479, 0.2407, 0.3385, 0.3103,
#     0.2844, 0.3083, 0.3032, 0.3053, 0.3048,
#     0.3555, 0.3275, 0.3672, 0.2712, 0.3693,
# ])


# full =  np.array([
#     0.2866, 0.3655, 0.4523, 0.2140, 0.2665,
#     0.3133, 0.2432, 0.2392, 0.3134, 0.3196,
#     0.3128, 0.3157, 0.3109, 0.3226, 0.2768,
#     0.3356, 0.5034, 0.3770, 0.2840, 0.3252,
# ])


#  KID
# close = np.array([
#     0.0713, 0.0975, 0.1134, 0.0494, 0.0892,
#     0.0788, 0.0234, 0.0356, 0.0853, 0.0838,
#     0.0744, 0.0643, 0.0532, 0.0686, 0.0658,
#     0.1164, 0.1061, 0.0643, 0.0618, 0.132
# ])

# lesion = np.array([
#     0.0516, 0.1239, 0.0774, 0.0442, 0.0631,
#     0.0857, 0.0453, 0.0336, 0.0778, 0.0762,
#     0.0584, 0.0650, 0.0647, 0.0570, 0.0584,
#     0.0926, 0.0853, 0.0468, 0.0511, 0.0812,
# ])

# full = np.array([
#     0.0909, 0.1051, 0.1097, 0.0549, 0.062,
#     0.0897, 0.0531, 0.0433, 0.0882, 0.086,
#     0.0837, 0.0695, 0.0739, 0.0763, 0.065,
#     0.0954, 0.2, 0.0583, 0.0672, 0.0926,
# ])

# DISTS
# close = np.array([
#     0.1968, 0.2336, 0.2733, 0.1712, 0.2119,
#     0.2141, 0.1098, 0.1427, 0.2116, 0.2193,
#     0.2055, 0.1953, 0.1836, 0.1988, 0.1978,
#     0.2333, 0.2187, 0.2159, 0.1942, 0.2397
# ])

# lesion = np.array([ 
#     0.2103, 0.3654, 0.2658, 0.1808, 0.2052,
#     0.2378, 0.1972, 0.1914, 0.2271, 0.2252,
#     0.2080, 0.2082, 0.2064, 0.2093, 0.2041,
#     0.2481, 0.2381, 0.2220, 0.1930, 0.2383
# ])

# full = np.array([
#     0.2124, 0.2355, 0.2669, 0.1742, 0.2064,
#     0.2211, 0.1846, 0.1861, 0.2152, 0.2177,
#     0.2188, 0.2082, 0.2072, 0.2116, 0.1988,
#     0.2368, 0.2871, 0.2196, 0.1981, 0.2243
# ])

# SSIM
close = np.array([
    0.8115, 0.4813, 0.4038, 0.8816, 0.7450,
    0.7055, 0.9100, 0.8621, 0.7299, 0.7132,
    0.7535, 0.7278, 0.7800, 0.7400, 0.7417,
    0.6757, 0.7241, 0.4299, 0.7785, 0.6507,
])

lesion = np.array([
    0.7583, 0.2031, 0.3897, 0.8805, 0.7895,
    0.6436, 0.7518, 0.7435, 0.6609, 0.7066,
    0.7667, 0.7311, 0.7428, 0.7250, 0.7420,
    0.6061, 0.6259, 0.4222, 0.7538, 0.6084,
])

full = np.array([
    0.7648, 0.5759, 0.4704, 0.5936, 0.6321,
    0.6321, 0.8045, 0.7557, 0.6978, 0.7077,
    0.7279, 0.6730, 0.6769, 0.6991, 0.7441,
    0.5999, 0.6163, 0.4105, 0.7052, 0.6505
])





models = [
    'Cycle_GAN', 'UNIT', 'MUNIT', 'StillGAN', 'CUT',
    'SRC', 'F-LSeSim/F', 'F-LSeSim/L', 'ConStructs', 'DCLGAN',
    'KAN-CUT', 'QS_Attn/G', 'QS_Attn/L', 'QS_Attn/L+G', 'FFPE++',
    'EnCO', 'AttentionGAN', 'GcGAN', 'StegoGAN', 'Santa'
]

x = np.arange(len(models))

#Replace the color as required.
colors = ["#ebc4f8", "#9974dc", "#693cbd"]  

data_sets = {
    'close': close,
    'lesion': lesion,
    'full': full
}
data_labels = ['CLOSE', 'LESION', 'FullSample']

top5_indices = {}
for name, data in data_sets.items():
    # top5_idx = np.argsort(data)[:5]
    top5_idx = np.argsort(data)[-5:]
    top5_indices[name] = top5_idx

fig, ax = plt.subplots(figsize=(18, 10))


for i, (name, data) in enumerate(data_sets.items()):
    color = colors[i]
    label = data_labels[i]
    ax.plot(x, data, color=color, label=label, marker='o', alpha=0.8)
    top5_idx = top5_indices[name]
    ax.scatter(x[top5_idx], data[top5_idx], color=colors[i], s=150, 
               marker='*', edgecolors='black', linewidth=0.5, zorder=10)


ax.set_title('SSIM Comparison of 20 Models on Three Datasets (Top 5 Performers Marked with Stars) ', 
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Model Name', fontsize=16, fontweight='500', labelpad=15)
ax.set_ylabel('SSIM Score (Higher is Better)', fontsize=16, fontweight='500', labelpad=15)


ax.set_xticks(x)
ax.set_xticklabels(models, rotation=60, ha='right', fontsize=9, rotation_mode='anchor')
ax.tick_params(axis='x', pad=8)

ax.tick_params(axis='y', labelsize=11)


ax.grid(True, linestyle='--', alpha=0.5, axis='y')
ax.set_axisbelow(True)


ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True, 
          bbox_to_anchor=(1.0, 1.0), borderaxespad=0.8)


all_data = np.concatenate([close, lesion, full])
ax.set_ylim(min(all_data) * 0.65, max(all_data) * 1.05)


plt.tight_layout()


plt.show()

fig.savefig('./Comparison Chart of SSIM Indexes Among Three Datasets.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')