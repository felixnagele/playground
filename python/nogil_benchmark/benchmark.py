import os
import subprocess
import sys
import threading
import time


def heavy_cpu_work(cycles: int) -> None:
    total: float = 0.0
    for i in range(cycles):
        total += (float(i) * 0.123) / 0.456


def run_metrics(num_threads: int) -> tuple[float, float]:
    cycles_per_thread: int = 20_000_000

    start: float = time.perf_counter()
    heavy_cpu_work(cycles_per_thread)
    t1_time: float = time.perf_counter() - start

    # Multi-Thread Run
    threads: list[threading.Thread] = [
        threading.Thread(target=heavy_cpu_work, args=(cycles_per_thread,))
        for _ in range(num_threads)
    ]

    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    tm_time: float = time.perf_counter() - start

    return t1_time, tm_time


if __name__ == "__main__":
    cpu_cores: int = os.cpu_count() or 4

    if len(sys.argv) > 1 and sys.argv[1] == "--collect":
        t1, tm = run_metrics(cpu_cores)
        print(f"{t1:.3f},{tm:.3f}")
        sys.exit(0)

    print(f"Found {cpu_cores} CPU cores.")
    print(f"Running benchmarks with all {cpu_cores} threads...")

    script_path = os.path.abspath(__file__)
    venv_bin_dir = "Scripts" if os.name == "nt" else "bin"
    venv_python = "python.exe" if os.name == "nt" else "python"

    # GIL ON
    classic_res = subprocess.run(
        [
            os.path.join(".venv-classic", venv_bin_dir, venv_python),
            script_path,
            "--collect",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    c_t1, c_tm = map(float, classic_res.stdout.strip().split(","))

    # GIL OFF
    nogil_env = os.environ.copy()
    nogil_env["PYTHON_GIL"] = "0"
    nogil_res = subprocess.run(
        [
            os.path.join(".venv-nogil", venv_bin_dir, venv_python),
            script_path,
            "--collect",
        ],
        capture_output=True,
        text=True,
        env=nogil_env,
        check=True,
    )
    n_t1, n_tm = map(float, nogil_res.stdout.strip().split(","))

    # Output
    metric_label: str = f"{cpu_cores} Threads Parallel"
    print(f"\n{'METRIC':<22} | {'3.14 CLASSIC (GIL)':<20} | {'3.15 NO-GIL':<20}")
    print("-" * 70)
    print(f"{'1 Thread':<22} | {c_t1:<16} sec | {n_t1:<16} sec")
    print(f"{metric_label:<22} | {c_tm:<16} sec | {n_tm:<16} sec")
    print("-" * 70)
    print(
        f"{'Scaling Overhead':<22} | {c_tm/c_t1:.2f}x execution time | {n_tm/n_t1:.2f}x execution time"
    )
