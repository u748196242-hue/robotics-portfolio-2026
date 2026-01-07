#!/usr/bin/env python3
import csv
from collections import defaultdict

CSV_PATH = "../results/results.csv"

def to_int(x):
    x = (x or "").strip()
    if x.upper() == "NA" or x == "":
        return None
    try:
        return int(float(x))
    except ValueError:
        return None

def to_float(x):
    x = (x or "").strip()
    if x.upper() == "NA" or x == "":
        return None
    try:
        return float(x)
    except ValueError:
        return None

def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r["setting"] = (r.get("setting") or "").strip()
            r["plan_success"] = to_int(r.get("plan_success"))
            r["exec_success"] = to_int(r.get("exec_success"))
            r["planning_time_s"] = to_float(r.get("planning_time_s"))
            rows.append(r)

    if not rows:
        print("No data rows found in", CSV_PATH)
        return

    by_setting = defaultdict(list)
    for r in rows:
        by_setting[r["setting"]].append(r)

    print("=== MoveIt2 A/B Summary ===")
    print(f"Total trials: {len(rows)}\n")

    for setting in sorted(by_setting.keys()):
        rs = by_setting[setting]
        n = len(rs)
        plan_ok = sum(1 for r in rs if r["plan_success"] == 1)
        plan_fail = sum(1 for r in rs if r["plan_success"] == 0)
        exec_ok = sum(1 for r in rs if r["exec_success"] == 1)
        exec_fail = sum(1 for r in rs if r["exec_success"] == 0)

        times = [r["planning_time_s"] for r in rs if isinstance(r["planning_time_s"], float)]
        times = [t for t in times if t is not None]

        print(f"[{setting}] trials={n}")
        print(f"  plan_success: {plan_ok}/{n} = {plan_ok/n:.2%} (fail={plan_fail})")
        print(f"  exec_success: {exec_ok}/{n} = {exec_ok/n:.2%} (fail={exec_fail})")
        if times:
            avg = sum(times)/len(times)
            mn = min(times)
            mx = max(times)
            print(f"  planning_time_s: n={len(times)}, avg={avg:.3f}, min={mn:.3f}, max={mx:.3f}")
        else:
            print("  planning_time_s: n=0 (all NA)")
        print()

    if "A" in by_setting and "B" in by_setting:
        A = by_setting["A"]; B = by_setting["B"]
        A_plan = sum(1 for r in A if r["plan_success"] == 1) / len(A)
        B_plan = sum(1 for r in B if r["plan_success"] == 1) / len(B)
        A_exec = sum(1 for r in A if r["exec_success"] == 1) / len(A)
        B_exec = sum(1 for r in B if r["exec_success"] == 1) / len(B)
        print("=== A vs B (quick) ===")
        print(f"Plan success: A={A_plan:.2%}, B={B_plan:.2%}")
        print(f"Exec success: A={A_exec:.2%}, B={B_exec:.2%}")

if __name__ == "__main__":
    main()
