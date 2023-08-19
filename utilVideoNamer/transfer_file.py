def transfer_file(file1, file2):
    """Transfers file1 to file2."""
    with open(file2, 'a') as transfer_to:
        with open(file1, 'r') as transfer_from:
            transfer_to.write(transfer_from.read())
        _clear_file(file1)


def _clear_file(file):
    with open(file, 'w'):
        ...


if __name__ == "__main__":
    transfer_file("a.txt", "b.txt")
