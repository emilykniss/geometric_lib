# calculate.py
import circle
import square
import triangle

figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {
    "area-circle": 1,
    "perimeter-circle": 1,
    "area-square": 1,
    "perimeter-square": 1,
    "area-triangle": 3,
    "perimeter-triangle": 3,
}


def calc(fig, func, size):

    if fig not in figs:
        raise ValueError(f"Invalid figure '{fig}'")
    if func not in funcs:
        raise ValueError(f"Invalid function '{func}'")
    if len(size) != sizes.get(f"{func}-{fig}", 1):
        raise ValueError(f"Invalid size parameters for {func} of {fig}")

    result = eval(f"{fig}.{func}(*{size})")
    return result
