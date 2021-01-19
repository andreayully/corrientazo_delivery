import delivery_routes


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    out_lines = delivery_routes.read_order_file()
    delivery_routes.write_out_file(out_lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
