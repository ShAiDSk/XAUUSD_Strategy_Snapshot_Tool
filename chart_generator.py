import matplotlib.pyplot as plt
import os
from datetime import datetime

def generate_snapshot(entry, sl, tp, rr_ratio):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axhline(entry, color='blue', linestyle='--', label=f"Entry: {entry}")
    ax.axhline(sl, color='red', linestyle='--', label=f"Stop Loss: {sl}")
    ax.axhline(tp, color='green', linestyle='--', label=f"Take Profit: {tp}")
    ax.fill_betweenx([sl, tp], 0, 1, color='green' if tp > entry else 'red', alpha=0.3)
    ax.set_title(f"XAUUSD Strategy Snapshot | RR: {rr_ratio}")
    ax.legend()
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    filename = f"snapshots/snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    os.makedirs("snapshots", exist_ok=True)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    return filename
