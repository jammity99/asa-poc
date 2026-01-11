
from pathlib import Path

def main():
    out_dir = Path("artifacts/demo")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "hello.txt").write_text("ASA should detect this file.\n", encoding="utf-8")
    print("[OK] Demo file created for ASA scan.")

if __name__ == "__main__":
    main()
