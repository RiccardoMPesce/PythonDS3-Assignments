import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ".lower()

def infinite_monkey(text):
    text_lower = text.lower()
    max_score = len(text)
    current_score = 0
    generated_string = ""

    n_generated = 0

    while True:
        rand_i = random.randint(0, len(alphabet) - 1)
        next_ch = alphabet[rand_i]
        n_generated += 1

        generated_string += next_ch
        if text_lower.startswith(generated_string):
            current_score = len(generated_string)
            if current_score == max_score:
                break
        else:
            current_score = 0
            generated_string = ""

    return n_generated


def main():
    s = "Ciao"
    ch_generated = infinite_monkey(s)
    print(f"Matching string '{s}' generated after {ch_generated} characters generated.")

if __name__ == "__main__":
    main()