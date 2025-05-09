# Find the product abc of the Pythagorean triplet for a + b + c = 1000
# Avoiding doing the math to just solve this directly :

# Solution : 31875000


def main() -> None:
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a * b * c)
                return


if __name__ == "__main__":
    main()
