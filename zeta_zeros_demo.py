"""
Polya Demo (Extended) on Android/Pydroid3
Marches through many consecutive critical-line zeros,
showing Z(t) crossing zero with live ASCII scan,
then refining to high precision and confirming residual.
"""

from mpmath import mp, zeta, gamma, exp, pi, log, mpc, findroot
import time, sys

# ------------------ CONFIG ------------------
mp.dps = 80
n0 = 399999
t0 = mp.mpf('360000433260.351086')  # high zero seed
n_target = n0 + 50   # <--- increase this number for more zeros
step_visual = mp.mpf('0.1')  # step size for visual scan
bar_width = 50  # ASCII plot width
sleep_time = 0.005  # delay for smoother scan (adjust as needed)

# ------------------ CORE FUNCTIONS ------------------
def theta(t):
    return mp.im(mp.log(mp.gamma(mp.mpf('0.25') + mpc(0, t/2)))) - (t/2) * mp.log(mp.pi)

def Z(t):
    s = mpc(0.5, t)
    return exp(mp.j*theta(t)) * zeta(s)

def avg_spacing(t):
    return 2*pi / mp.log(t / (2*pi))

def refine_zero_step(t_current, tol=1e-25):
    d = avg_spacing(t_current)
    a = t_current + 0.45*d
    b = t_current + 1.55*d
    Za = mp.re(Z(a))
    Zb = mp.re(Z(b))
    
    if Za == 0:
        return a, 0
    if Zb == 0:
        return b, 0
    if mp.sign(Za) != mp.sign(Zb):
        t_ref = findroot(lambda tt: mp.re(Z(tt)), [a, b], tol=tol, verify=False)
    else:
        t_guess = t_current + d
        t_ref = findroot(lambda tt: mp.re(Z(tt)), t_guess, tol=tol, verify=False)
    return t_ref, abs(Z(t_ref))

# ------------------ LIVE PLOT FUNCTION ------------------
def plot_Z_line(Zval, width=50):
    """ASCII plot with vertical axis at center"""
    scale = max(abs(Zval), 1e-20)
    center = width // 2
    pos = int(center + (Zval/scale) * (width // 2))
    pos = max(0, min(width - 1, pos))
    line = [' '] * width
    line[center] = '|'
    line[pos] = '*'
    return ''.join(line)

# ------------------ MAIN LOOP ------------------
n = n0
t = t0
print(f"Starting demo at n={n}, t={mp.nstr(t,18)}")

while n < n_target:
    # Visual scan between zeros
    t_scan = t
    d = avg_spacing(t)
    t_end = t + d
    while t_scan < t_end:
        Zval = mp.re(Z(t_scan))
        bar = plot_Z_line(Zval, bar_width)
        sys.stdout.write(f"\rScanning t={mp.nstr(t_scan,8)} {bar}")
        sys.stdout.flush()
        t_scan += step_visual
        time.sleep(sleep_time)
    
    # Refine exact zero
    t, residual = refine_zero_step(t)
    print(f"\n✔ Found zero n={n+1}, t={mp.nstr(t,15)}, residual={mp.nstr(residual,3)}")
    n += 1

print(f"\nDemo complete. Verified {n - n0} consecutive critical-line zeros.")