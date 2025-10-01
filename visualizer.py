import matplotlib.pyplot as plt
import io
import base64

def plot_equity_curve(equity_curve):
    fig, ax = plt.subplots(figsize=(10,5))
    equity_curve.plot(ax=ax, title="Equity Curve", color="blue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value")

    # Save plot to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return img_b64
