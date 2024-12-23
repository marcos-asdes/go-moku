import subprocess

def main():
    subprocess.run(["pytest", "--cov=src", "--cov-report=term-missing", "--cov-report=html"])

if __name__ == "__main__":
    main()