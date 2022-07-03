def bool_expression(a, b, c):
    a = bool(a)
    b = bool(b)
    c = bool(c)

    # a & b -> c
    result = (not (a and b)) or c

    return result


def table(bool_expr):
    from prettytable import PrettyTable
    th = ["A", "B", "C", str(bool_expr)]
    table = PrettyTable(th)
    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                table.add_row((str(a), str(b), str(c), str(bool_expression(a, b, c))))
    
    print(table)


if __name__ == "__main__":
    table("a & b -> c")