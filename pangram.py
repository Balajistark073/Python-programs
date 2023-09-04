def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(s.lower()) >= alphabet
def main():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        s = input(f"Enter string {i + 1}: ")
        strings.append(s)
    output_sequence = ""
    for s in strings:
        if is_pangram(s):
            output_sequence += "1"
        else:
            output_sequence += "0"
    print("Output sequence:", output_sequence)
if __name__ == "__main__":
    main()
