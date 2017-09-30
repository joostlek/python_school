def safe_input(str):
    try:
        return input(str)
    except KeyboardInterrupt:
        return

safe_input('lol')