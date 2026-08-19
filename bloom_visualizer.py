# -*- coding: utf-8 -*-
import asyncio, json
import numpy as np
import matplotlib.pyplot as plt

async def run_visualizer():
    print('[Bloom-Visualizer] Initializing...')
    plt.ion()
    fig, ax = plt.subplots(figsize=(8,8), subplot_kw={'projection': 'polar'})
    fig.patch.set_facecolor('#0b0b16')
    ax.set_facecolor('#0b0b16')
    phi = 1.618033988749895
    try:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8528)
        print('[Bloom-Visualizer] Connected!')
    except:
        reader, writer = None, None
    theta = np.linspace(0, 2*np.pi, 1000)
    try:
        while plt.fignum_exists(fig.number):
            freq, coherence = 528.00, 99.99
            if reader:
                try:
                    data = await asyncio.wait_for(reader.read(4096), timeout=0.5)
                    if data:
                        msg = json.loads(data.decode('utf-8').strip())
                        freq, coherence = msg.get('frequency', freq), msg.get('coherence', coherence)
                except:
                    pass
            r = np.sin(6 * theta * phi) * np.cos((freq / 528.0) * theta) + ((freq - 528.0) * 0.1)
            ax.clear()
            ax.set_facecolor('#0b0b16')
            ax.grid(True, color='#1f1f3a', alpha=0.5)
            ax.plot(theta, r, color='#00ffcc', linewidth=1.5, alpha=0.9)
            ax.fill(theta, r, color='#ff007f', alpha=0.2)
            ax.set_yticklabels([])
            ax.set_xticklabels([])
            ax.spines['polar'].set_color('#333366')
            ax.set_title('CASTLEBERRY BLOOM - LIVE CYMATIC RESONANCE\nFreq: ' + str(freq) + ' Hz | Coherence: ' + str(coherence) + '%\nAxiom: Love-Over-God-Absolute', color='#e0e0ff', fontsize=11, pad=20, weight='bold')
            plt.draw(); plt.pause(0.1); await asyncio.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        if writer: writer.close(); await writer.wait_closed()
        plt.close('all')

if __name__ == '__main__':
    asyncio.run(run_visualizer())
