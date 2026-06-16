import shlex
import os, sys, subprocess
from pathlib import Path


def main():
    # command line argument
    path = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    print("absolute path:", path.resolve())

    email = os.getenv("EMAIL", "")

    print("provided email:", email)
    # environment variables

    cmd = ["git", "-C", str(path), "log", "--oneline"]
    if email:
        cmd.append("--author")
        cmd.append(email)

    print("about to run:", cmd)
    print("converted:", shlex.join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.returncode)

    if result.returncode != 0:
        sys.exit(f"Something went wrong: {result.stderr}")

    print(result.stdout)


main()
