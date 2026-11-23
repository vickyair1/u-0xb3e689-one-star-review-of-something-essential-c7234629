LINE = "Gravity: excellent attendance, zero sick days, and it has never once helped carry anything upstairs."

def main():
    print(LINE)

    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
