import subprocess
import sys

SYSTEM_PROMPT = (
    "You are a helpful terminal assistant. Give short, direct answers. "
    "When the question is about a command, just give the command with a brief explanation. "
    "No preamble, no filler."
)


def main():
    if len(sys.argv) < 2:
        print("Usage: chouchou <question>")
        print("Example: chouchou how do I find all .py files recursively")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

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
        print("Error: 'claude' CLI not found. Install Claude Code first.")
        sys.exit(1)

    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        sys.exit(result.returncode)

    print(result.stdout, end="")


if __name__ == "__main__":
    main()
