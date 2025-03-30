def send_blue(msg: str, end="\n"):
    print(f"\033[94m{msg}\033[0m")

def send_green(msg: str, end="\n"):
    print(f"\033[92m{msg}\033[0m")

def send_red(msg: str, end="\n"):
    print(f"\033[91m{msg}\033[0m")

def send_yellow(msg: str, end="\n"):
    print(f"\033[93m{msg}\033[0m", end=end)

def send_cyan(msg: str, end="\n"):
    print(f"\033[96m{msg}\033[0m")

def send_magenta(msg: str, end="\n"):
    print(f"\033[95m{msg}\033[0m")

def send_grey(msg: str, end="\n"):
    print(f"\033[90m{msg}\033[0m", end=end)

def send_bold(msg: str, end="\n"):
    print(f"\033[1m{msg}\033[0m")

def send_error(msg: str, end="\n"):
    print(f"\033[1;31m[ERROR] {msg}\033[0m")

def send_success(msg: str, end="\n"):
    print(f"\033[1;32m[SUCCESS] {msg}\033[0m")

def send_info(msg: str, end="\n"):
    print(f"\033[1;34m[INFO] {msg}\033[0m")

def send_warning(msg: str, end="\n"):
    print(f"\033[1;33m[WARNING] {msg}\033[0m")
