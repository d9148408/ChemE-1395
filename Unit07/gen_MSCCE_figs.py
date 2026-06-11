"""
Generate theory figures for Unit07_MSCCE (Multistage Countercurrent Extraction)

Figures produced:
  fig_MSCCE_0a.png   - Cross-flow extraction schematic (N=3 stages)
  fig_MSCCE_0b.png   - Countercurrent extraction schematic (N=3 stages)
  fig_MSCCE_YX.png   - Y-X operating diagram with McCabe-Thiele stepping
  fig_MSCCE_recovery.png - Recovery rate comparison (single/cross-flow/countercurrent)

Run: python gen_MSCCE_figs.py  (PY310 env)
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ── output directory ──────────────────────────────────────────────────────────
OUT = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT, exist_ok=True)

matplotlib.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.unicode_minus': False,
})

# ─────────────────────────────────────────────────────────────────────────────
# Helper: draw arrow with optional mid-label
# ─────────────────────────────────────────────────────────────────────────────
def arrow(ax, x1, y1, x2, y2, color='black', lw=1.8, label='', fs=9,
          label_offset=(0, 0.12)):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))
    if label:
        mx = (x1 + x2) / 2 + label_offset[0]
        my = (y1 + y2) / 2 + label_offset[1]
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=fs,
                color=color)


def stage_box(ax, cx, cy, w, h, label, bg='#d6e8f7', ec='#2c5f8e'):
    rect = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                          boxstyle="round,pad=0.07", linewidth=1.8,
                          edgecolor=ec, facecolor=bg, zorder=3)
    ax.add_patch(rect)
    ax.text(cx, cy, label, ha='center', va='center', fontsize=12,
            fontweight='bold', color=ec, zorder=4)


# ─────────────────────────────────────────────────────────────────────────────
# Figure MSCCE-0a : Cross-flow extraction schematic
# ─────────────────────────────────────────────────────────────────────────────
def fig_crossflow():
    fig, ax = plt.subplots(figsize=(11, 4.4))
    ax.set_xlim(-0.3, 11)
    ax.set_ylim(-0.7, 4.3)
    ax.axis('off')

    N = 3
    bw, bh = 1.55, 1.25
    cy = 1.8                     # stage box centre y
    xs = [1.8, 5.0, 8.2]        # stage centre x

    # ── stage boxes ──────────────────────────────────────────────────────────
    for i, x in enumerate(xs):
        stage_box(ax, x, cy, bw, bh, f'Stage {i+1}')

    # ── raffinate path (left → right) ────────────────────────────────────────
    # Feed
    arrow(ax, 0.0, cy, xs[0] - bw/2, cy, color='#1a6b1a', lw=2,
          label='Feed\n($X_F$)', label_offset=(0, 0.2))
    # between stages
    for i in range(N - 1):
        x1, x2 = xs[i] + bw/2, xs[i+1] - bw/2
        arrow(ax, x1, cy, x2, cy, color='#1a6b1a', lw=2,
              label=f'$R_{i+1}$', label_offset=(0, 0.18))
    # raffinate product
    arrow(ax, xs[-1] + bw/2, cy, 10.8, cy, color='#1a6b1a', lw=2,
          label='Raffinate\n($X_R$)', label_offset=(0, 0.2))

    # ── fresh solvent entering from top ──────────────────────────────────────
    for i, x in enumerate(xs):
        arrow(ax, x, 3.85, x, cy + bh/2, color='#8b1a8b', lw=1.8,
              label=f'$S_{{\\rm tot}}/{N}$\n(fresh)', fs=8.5,
              label_offset=(0, 0.1))

    # ── extract leaving from bottom ──────────────────────────────────────────
    for i, x in enumerate(xs):
        arrow(ax, x, cy - bh/2, x, -0.05, color='#b85800', lw=1.8,
              label=f'$E_{i+1}$', fs=9, label_offset=(0, -0.22))

    # ── combined extract label ────────────────────────────────────────────────
    ax.text(5.0, -0.55, 'Combined Extract   ($E_1 + E_2 + E_3$)',
            ha='center', va='center', fontsize=10, color='#b85800', style='italic')

    # ── solvent annotation ────────────────────────────────────────────────────
    ax.text(5.0, 4.15,
            f'Total Solvent $S_{{\\rm tot}}$ divided equally into {N} portions',
            ha='center', va='center', fontsize=9.5, color='#8b1a8b', style='italic')

    ax.set_title('(a) Cross-flow Extraction — N = 3 Stages,  Fresh Solvent at Every Stage',
                 fontsize=12, fontweight='bold', pad=6)
    plt.tight_layout()
    out = os.path.join(OUT, 'fig_MSCCE_0a.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'Saved {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Figure MSCCE-0b : Countercurrent extraction schematic
# ─────────────────────────────────────────────────────────────────────────────
def fig_countercurrent():
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.set_xlim(-0.3, 11)
    ax.set_ylim(-0.5, 4.8)
    ax.axis('off')

    N = 3
    bw, bh = 1.55, 1.55
    xs = [1.8, 5.0, 8.2]
    cy = 2.0
    rY = cy + 0.62        # raffinate stream y (upper lane)
    sY = cy - 0.62        # solvent/extract stream y (lower lane)

    # ── stage boxes ──────────────────────────────────────────────────────────
    for i, x in enumerate(xs):
        stage_box(ax, x, cy, bw, bh, f'Stage {i+1}')

    # ── raffinate path: Feed → Stage 1 → ... → Stage N → Raffinate ──────────
    arrow(ax, 0.0, rY, xs[0] - bw/2, rY, color='#1a6b1a', lw=2,
          label='Feed\n($X_F$)', label_offset=(0, 0.18))
    for i in range(N - 1):
        x1, x2 = xs[i] + bw/2, xs[i+1] - bw/2
        arrow(ax, x1, rY, x2, rY, color='#1a6b1a', lw=2,
              label=f'$R_{i+1}$', label_offset=(0, 0.18))
    arrow(ax, xs[-1] + bw/2, rY, 10.8, rY, color='#1a6b1a', lw=2,
          label='Raffinate\n($X_R$)', label_offset=(0, 0.18))

    # ── solvent/extract path: Solvent → Stage N → ... → Stage 1 → Extract ────
    arrow(ax, 10.8, sY, xs[-1] + bw/2, sY, color='#8b1a8b', lw=2,
          label='Solvent\n($Y_S=0$)', label_offset=(0, -0.22))
    for i in range(N - 1, 0, -1):
        x1, x2 = xs[i] - bw/2, xs[i-1] + bw/2
        arrow(ax, x1, sY, x2, sY, color='#8b1a8b', lw=2,
              label=f'$L_{i}$', label_offset=(0, -0.22))
    arrow(ax, xs[0] - bw/2, sY, 0.0, sY, color='#8b1a8b', lw=2,
          label='Extract\n($Y_E$)', label_offset=(0, -0.22))

    # ── direction labels ──────────────────────────────────────────────────────
    ax.annotate('', xy=(10.6, rY + 0.55), xytext=(0.2, rY + 0.55),
                arrowprops=dict(arrowstyle='->', color='#1a6b1a', lw=1.2, ls='dashed'))
    ax.text(5.3, rY + 0.7, 'Raffinate / Feed Phase  →', ha='center',
            fontsize=9, color='#1a6b1a', style='italic')

    ax.annotate('', xy=(0.2, sY - 0.52), xytext=(10.6, sY - 0.52),
                arrowprops=dict(arrowstyle='->', color='#8b1a8b', lw=1.2, ls='dashed'))
    ax.text(5.3, sY - 0.68, '←  Solvent / Extract Phase', ha='center',
            fontsize=9, color='#8b1a8b', style='italic')

    ax.set_title('(b) Countercurrent Extraction — N = 3 Stages,  Single Solvent Pass',
                 fontsize=12, fontweight='bold', pad=6)
    plt.tight_layout()
    out = os.path.join(OUT, 'fig_MSCCE_0b.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'Saved {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Figure MSCCE-YX : Y-X McCabe-Thiele diagram  (E=2.0, m=1.5, N=3 stages)
# ─────────────────────────────────────────────────────────────────────────────
def fig_YX_mccabe():
    fig, ax = plt.subplots(figsize=(7.5, 6.5))

    # ── parameters ────────────────────────────────────────────────────────────
    m   = 1.5      # KLL (equilibrium slope)
    E   = 2.0      # extraction factor
    XF  = 0.50     # feed mole ratio
    YS  = 0.00     # fresh solvent (no solute)

    FoS = m / E    # F'/S' = 0.75

    # Kremser: η = E(E^N-1)/(E^(N+1)-1), N=3
    N_stages = 3
    eta = E * (E**N_stages - 1) / (E**(N_stages+1) - 1)
    XR  = XF * (1 - eta)
    YE  = FoS * (XF - XR) + YS

    Xmax = XF * 1.18
    Xv   = np.linspace(0, Xmax, 400)

    # ── equilibrium line ──────────────────────────────────────────────────────
    ax.plot(Xv, m * Xv, color='#1a5faa', lw=2.5,
            label=f'Equilibrium Line  ($Y^* = {m}\\,X$,  $KLL = {m}$)')

    # ── operating line ────────────────────────────────────────────────────────
    Y_op = FoS * Xv + (YE - FoS * XF)
    ax.plot(Xv, Y_op, color='#c0392b', lw=2.5,
            label=f'Operating Line  (slope $F\'/S\' = {FoS:.2f}$,  $E = {E:.1f}$)')

    # ── minimum solvent line (pinch at feed end) ───────────────────────────────
    Yeq_at_XF = m * XF   # = 0.75
    ax.plot([XR, XF], [YS, Yeq_at_XF], color='gray', lw=1.4, ls=':',
            label=f'Min-Solvent Line  (pinch at $X_F$,  $S\'_{{\\min}}$)')

    # ── McCabe-Thiele stepping ─────────────────────────────────────────────────
    # Direction: from (XF, YE) rightmost on op-line → step to (XR, YS)
    # Horizontal step: go from operating-line point to equilibrium curve (same Y → new X)
    # Vertical step:   go from equilibrium point to operating line (same X → new Y)
    path_x = [XF]
    path_y = [YE]
    X_cur  = XF
    Y_cur  = YE
    stage_eq_pts = []   # (X_eq, Y_eq) for each stage

    for s in range(N_stages + 2):
        # Horizontal → equilibrium curve
        X_eq = Y_cur / m
        path_x.append(X_eq)
        path_y.append(Y_cur)          # Y unchanged (horizontal)
        stage_eq_pts.append((X_eq, Y_cur))
        X_cur = X_eq
        if X_cur <= XR * 1.02:
            break
        # Vertical → operating line
        Y_new = FoS * X_cur + (YE - FoS * XF)
        path_x.append(X_cur)
        path_y.append(Y_new)          # X unchanged (vertical)
        Y_cur = Y_new

    ax.plot(path_x, path_y, color='#27ae60', lw=2.0, alpha=0.9, zorder=5,
            label=f'McCabe-Thiele Steps  ($N = {N_stages}$ stages,  $\\eta = {eta*100:.1f}\\%$)')

    # ── stage equilibrium points ───────────────────────────────────────────────
    for i, (px, py) in enumerate(stage_eq_pts[:N_stages]):
        ax.plot(px, py, 'o', color='#27ae60', ms=9, zorder=6)
        ax.text(px + 0.008, py + 0.015, f'Stage {i+1}',
                fontsize=9.5, color='#1a7a1a', va='bottom', ha='left')

    # ── terminal operating points ─────────────────────────────────────────────
    ax.plot(XF, YE, '^', color='#c0392b', ms=11, zorder=7,
            label=f'Feed end  ($X_F={XF}$,  $Y_E={YE:.3f}$)')
    ax.plot(XR, YS, 's', color='#c0392b', ms=11, zorder=7,
            label=f'Solvent end  ($X_R={XR:.3f}$,  $Y_S={YS}$)')

    # ── dashed guides to axes ─────────────────────────────────────────────────
    for xv, yv in [(XF, YE), (XR, YS)]:
        ax.plot([xv, xv], [0, yv], 'k--', lw=0.7, alpha=0.45)
        ax.plot([0, xv], [yv, yv], 'k--', lw=0.7, alpha=0.45)

    # ── operating region shading ──────────────────────────────────────────────
    Xfill  = np.linspace(XR, XF, 200)
    Y_eq_f = m * Xfill
    Y_op_f = FoS * Xfill + (YE - FoS * XF)
    ax.fill_between(Xfill, Y_op_f, Y_eq_f, alpha=0.08, color='#27ae60',
                    label='Driving force region')

    # ── axis labels & formatting ──────────────────────────────────────────────
    ax.set_xlabel('$X$   [mol solute / mol diluent]', fontsize=13)
    ax.set_ylabel('$Y$   [mol solute / mol solvent]', fontsize=13)
    ax.set_title(
        f'Y-X Operating Diagram — Countercurrent Extraction\n'
        f'McCabe-Thiele Stepping  '
        f'($KLL = {m}$,   $E = {E}$,   $N = {N_stages}$ stages,   $\\eta = {eta*100:.1f}\\%$)',
        fontsize=12, fontweight='bold')
    ax.set_xlim(0, Xmax)
    ax.set_ylim(0, m * Xmax * 1.08)
    ax.legend(fontsize=8.5, loc='upper left', framealpha=0.9)
    ax.grid(True, alpha=0.28)
    ax.set_facecolor('#f9f9f9')

    # ── pinch annotation ──────────────────────────────────────────────────────
    ax.annotate('Pinch point\n($X_F$, $mX_F$)',
                xy=(XF, Yeq_at_XF), xytext=(XF - 0.08, Yeq_at_XF + 0.04),
                fontsize=8.5, color='gray',
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.0))

    plt.tight_layout()
    out = os.path.join(OUT, 'fig_MSCCE_YX.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'Saved {out}')


# ─────────────────────────────────────────────────────────────────────────────
# Figure MSCCE-recovery : Recovery rate comparison (two panels)
# ─────────────────────────────────────────────────────────────────────────────
def fig_recovery_compare():
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.8))
    fig.subplots_adjust(wspace=0.30)

    E_arr = np.linspace(0.05, 5.0, 600)
    N_ref = 3   # fixed N for left panel

    # ── helper functions ──────────────────────────────────────────────────────
    def eta_single(E):
        return E / (1 + E)

    def eta_crossflow(E, N):
        return 1 - (N / (N + E)) ** N

    def eta_counter(E, N):
        """Countercurrent Kremser recovery (handles E=1)."""
        result = np.where(
            np.abs(E - 1) < 1e-5,
            N / (N + 1),
            E * (E**N - 1) / (E**(N+1) - 1)
        )
        return result

    # ──────────────────────────────────────────────────────────────────────────
    # Panel A: Fixed N=3, vary E
    # ──────────────────────────────────────────────────────────────────────────
    ax = axes[0]
    ax.plot(E_arr, eta_single(E_arr) * 100,
            'b--', lw=2.0, alpha=0.8, label='Single Stage ($N=1$)')
    ax.plot(E_arr, eta_crossflow(E_arr, N_ref) * 100,
            color='#e67e00', lw=2.0, ls='-.', alpha=0.85,
            label=f'Cross-flow ($N={N_ref}$)')
    ax.plot(E_arr, eta_counter(E_arr, N_ref) * 100,
            'g-', lw=2.5, label=f'Countercurrent ($N={N_ref}$)')

    # reference verticals / horizontals
    ax.axvline(1.0,  color='gray', lw=0.9, ls=':', alpha=0.7)
    ax.axvline(1.5,  color='gray', lw=0.9, ls=':', alpha=0.5)
    ax.axhline(90.0, color='#d35400', lw=0.9, ls='--', alpha=0.6)
    ax.text(0.07, 91, '90 %', fontsize=8.5, color='#d35400')
    ax.text(1.02, 3, '$E=1$',   fontsize=8.5, color='gray')
    ax.text(1.52, 3, '$E=1.5$', fontsize=8.5, color='gray')

    # annotate E=1.5
    E_mark = 1.5
    for fn, col in [(eta_single, 'blue'), (eta_crossflow, '#e67e00'),
                    (eta_counter, 'green')]:
        y_val = (fn(E_mark, N_ref) if fn != eta_single else fn(E_mark)) * 100
        ax.plot(E_mark, y_val, 'o', color=col, ms=7, zorder=5)
    # callout
    ys = [eta_single(E_mark)*100, eta_crossflow(E_mark, N_ref)*100,
          eta_counter(E_mark, N_ref)*100]
    labels = ['60.0 %', '70.4 %', '87.7 %']
    offsets = [(-0.35, -6), (-0.35, 5), (0.08, 3)]
    colors  = ['blue', '#e67e00', 'green']
    for (ox, oy), lb, col, yv in zip(offsets, labels, colors, ys):
        ax.text(E_mark + ox, yv + oy, lb, fontsize=8.5, color=col, fontweight='bold')

    ax.set_xlabel('Extraction Factor $E$', fontsize=12)
    ax.set_ylabel('Solute Recovery $\\eta$ / %', fontsize=12)
    ax.set_title(f'Recovery vs. Extraction Factor\n(Fixed $N = {N_ref}$ stages)',
                 fontsize=11, fontweight='bold')
    ax.legend(fontsize=9.5, loc='lower right')
    ax.set_xlim(0.05, 5.0)
    ax.set_ylim(0, 103)
    ax.grid(True, alpha=0.28)

    # ──────────────────────────────────────────────────────────────────────────
    # Panel B: Fixed E=1.5, vary N
    # ──────────────────────────────────────────────────────────────────────────
    ax = axes[1]
    E_fix = 1.5
    N_arr = np.arange(1, 11)

    ys_cf  = np.array([eta_crossflow(E_fix, n) for n in N_arr]) * 100
    ys_cc  = np.array([eta_counter(E_fix, n)   for n in N_arr]) * 100
    ys_s1  = eta_single(E_fix) * 100

    ax.axhline(ys_s1, color='blue', lw=1.8, ls='--', alpha=0.7,
               label=f'Single Stage (ref.  $\\eta={ys_s1:.1f}\\%$)')
    ax.plot(N_arr, ys_cf, 's-', color='#e67e00', lw=2.0, ms=8,
            label=f'Cross-flow ($E={E_fix}$)')
    ax.plot(N_arr, ys_cc, 'o-', color='green', lw=2.5, ms=8,
            label=f'Countercurrent ($E={E_fix}$)')

    ax.axhline(90,  color='#d35400', lw=0.9, ls='--', alpha=0.6)
    ax.axhline(99,  color='purple',  lw=0.9, ls=':',  alpha=0.55)
    ax.text(0.6,  91, '90 %', fontsize=8.5, color='#d35400')
    ax.text(0.6, 99.4, '99 %', fontsize=8.5, color='purple')

    # annotate N=3
    for arr, col in [(ys_cf, '#e67e00'), (ys_cc, 'green')]:
        ax.annotate(f'{arr[2]:.1f}%',
                    xy=(3, arr[2]), xytext=(3.3, arr[2] - 5),
                    fontsize=8.5, color=col, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=col, lw=1))

    ax.set_xlabel('Number of Theoretical Stages $N$', fontsize=12)
    ax.set_ylabel('Solute Recovery $\\eta$ / %', fontsize=12)
    ax.set_title(f'Recovery vs. Number of Stages\n(Fixed $E = {E_fix}$)',
                 fontsize=11, fontweight='bold')
    ax.legend(fontsize=9.5, loc='lower right')
    ax.set_xlim(0.5, 10.5)
    ax.set_ylim(0, 103)
    ax.set_xticks(N_arr)
    ax.grid(True, alpha=0.28)

    fig.suptitle(
        'Extraction Mode Comparison:  Single Stage  vs.  Cross-flow  vs.  Countercurrent',
        fontsize=13, fontweight='bold', y=1.01)

    out = os.path.join(OUT, 'fig_MSCCE_recovery.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'Saved {out}')


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    fig_crossflow()
    fig_countercurrent()
    fig_YX_mccabe()
    fig_recovery_compare()
    print('\nAll theory figures generated successfully.')
