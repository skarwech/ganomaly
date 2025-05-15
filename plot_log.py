import matplotlib.pyplot as plt
import re

# Read the log file
with open("output\ganomaly\mnist\loss_log.txt", "r") as f:
    log_lines = f.readlines()

# Extract ROC and Max ROC values using regex
steps, roc_values, max_roc_values = [], [], []
for idx, line in enumerate(log_lines):
    match = re.search(r'roc: (\d+\.\d+).*max roc: (\d+\.\d+)', line)
    if match:
        steps.append(idx + 1)  # Use line index as step (or epoch)
        roc_values.append(float(match.group(1)))
        max_roc_values.append(float(match.group(2)))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(steps, roc_values, marker='o', linestyle='-', color='blue', label='ROC Abderrahim')
plt.plot(steps, max_roc_values, marker='o', linestyle='-', color='red', label='ROC article')
plt.xlabel("Step/Batch/Epoch")
plt.ylabel("ROC Value")
plt.title("Evolution of ROC")
plt.grid(True)
plt.legend()
plt.show()

# steps, avg_times = [], []
# for idx, line in enumerate(log_lines):
#     match = re.search(r'Avg Run Time \(ms/batch\): (\d+\.\d+)', line)
#     if match:
#         steps.append(idx + 1)  # Use line index as step/epoch
#         avg_times.append(float(match.group(1)))

# total_time_ms = sum(avg_times)*64*15*15  # Assuming 64 batches per epoch
# total_time_sec = total_time_ms / 1000  # Convert ms to seconds
# total_time_min = total_time_sec / (3600*24)   # Convert to minutes (optional)


# # Plot
# plt.figure(figsize=(10, 6))
# plt.plot(steps, avg_times, marker='o', linestyle='-', color='green', label='Avg Time per Batch')
# text = f"Total Time: {total_time_min:.2f} days)"
# plt.annotate(
#     text,
#     xy=(0.95, 0.95),                   # Position (x, y) in axes coordinates (right-top)
#     xycoords='axes fraction',
#     ha='right', va='top',
#     fontsize=12,
#     bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
# )

# plt.xlabel("Step/Batch/Epoch")
# plt.ylabel("Time (s/batch)")
# plt.title("Evolution of Average Run Time per Batch")
# plt.grid(True)
# plt.legend()
# plt.show()