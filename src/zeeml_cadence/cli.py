import json
import sys
from . import analyze_cadence


def main():
    text = " ".join(sys.argv[1:]).strip()
    if not text:
        print("Usage: zeeml-cadence <text>  |  Web studio: https://zeeml.com/ai-humanizer")
        return
    print(json.dumps(analyze_cadence(text), indent=2))


if __name__ == "__main__":
    main()
