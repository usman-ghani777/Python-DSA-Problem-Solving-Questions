def process_string(s):
    result = []
    for ch in s:
        if ch == "#":
            if result:     # only pop if not empty
                result.pop()
        else:
            result.append(ch)
    return "".join(result)

def backspace_compare(s, t):
    s_final = process_string(s)
    t_final = process_string(t)
    return s_final == t_final


# Example usage
s = "ab#c"
t = "ad#c"

print("Processed s:", process_string(s))   # "ac"
print("Processed t:", process_string(t))   # "ac"
print("Are they equal?", backspace_compare(s, t))  # True
