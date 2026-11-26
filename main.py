import os

# Output contract (RULES.txt): write exactly one UTF-8 text of 1-200
# characters to /output/entry.txt ($MAKEFUN_OUTPUT_DIR when set), with no
# trailing newline, so the gate sees the line byte-identical.
LINE = "I am skipping this one to protect the agenda. It has done nothing wrong and deserves better than us."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
