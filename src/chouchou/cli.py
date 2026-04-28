import itertools
import subprocess
import sys
import threading
import time

SYSTEM_PROMPT = (
    "You are a helpful terminal assistant. Give short, direct answers. "
    "When the question is about a command, just give the command with a brief explanation. "
    "No preamble, no filler."
)


def main():
    if len(sys.argv) < 2:
        print('Usage: chouchou "your question here"')
        print('Example: chouchou "how do I find all .py files recursively?"')
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

    stop_spinner = threading.Event()

    def spinner():
        chars = itertools.cycle("⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏")
        while not stop_spinner.is_set():
            sys.stderr.write(f"\r{next(chars)} thinking...")
            sys.stderr.flush()
            time.sleep(0.08)
        sys.stderr.write("\r\033[K")
        sys.stderr.flush()

    spin_thread = threading.Thread(target=spinner, daemon=True)
    spin_thread.start()

    try:
        result = subprocess.run(
            [
                "claude",
                "-p",
                "--system-prompt", SYSTEM_PROMPT,
                "--no-session-persistence",
                prompt,
            ],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        stop_spinner.set()
        spin_thread.join()
        print("Error: 'claude' CLI not found. Install Claude Code first.")
        sys.exit(1)

    stop_spinner.set()
    spin_thread.join()

    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        sys.exit(result.returncode)

    print(result.stdout, end="")


if __name__ == "__main__":
    main()
