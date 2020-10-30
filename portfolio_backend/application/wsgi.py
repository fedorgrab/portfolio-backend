# fmt: off
import os
import sys

print("ASODASDASDASDASDASDASD")
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "../", "../")))

from portfolio_backend.application import backend_application  # noqa

if __name__ == "__main__":
    backend_application.run(host="0.0.0.0")
