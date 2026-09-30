import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def scatter_save(x, y, xlabel, ylabel, title, path):
    if not x or not y:
        return False
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()
    return True


if __name__ == "__main__":
    scatter_save([1, 2], [3, 4], "x", "y", "Test", "plots/_scatter_test.png")
