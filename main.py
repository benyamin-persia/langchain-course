import os  # built-in: read env vars like OPENAI_API_KEY via os.getenv()

from dotenv import \
    load_dotenv  # loads key=value pairs from .env into the process environment

load_dotenv()  # reads .env so secrets are available without hardcoding them


def main():
    print(
        os.getenv("OPENAI_API_KEY")
    )  # prints the key loaded from .env (course demo only — don't log secrets in real apps)


if __name__ == "__main__":
    main()
