"""Run the Cangjie CLI with UTF-8 inherited by subprocesses on Windows."""

import os
from pathlib import Path
import subprocess
import sys


def main() -> int:
    tool = Path(__file__).resolve().with_name('cangjie.py')
    if not tool.is_file():
        raise SystemExit('Cangjie CLI was not found beside this entry point')
    task_env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
    return subprocess.call([sys.executable, str(tool), *sys.argv[1:]], env=task_env)


if __name__ == '__main__':
    raise SystemExit(main())
