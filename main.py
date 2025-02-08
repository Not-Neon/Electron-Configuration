atomic_no = int(input("Enter the Periodic Number of the element (max = 118): "))

# Check if the input is within valid range
if atomic_no < 1 or atomic_no > 118:
    print("\nInvalid input! Please enter a number between 1 and 118.")
    input("Press any key to exit...")
    exit()

# Creating the default subshell array up to 118 naturally occurring elements
subshell = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s",
            "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
config = ""  # Empty string

# Creating exception element config strings
exceptions = {
    24: "1s2 2s2 2p6 3s2 3p6 4s1 3d5",      # Chromium
    29: "1s2 2s2 2p6 3s2 3p6 4s1 3d10",     # Copper
    41: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4",  # Niobium
    42: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5",  # Molybdenum
    44: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7",  # Ruthenium
    45: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8",  # Rhodium
    46: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10",     # Palladium
    47: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10", # Silver
    57: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1",  # Lanthanum
    58: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1 5d1",  # Cerium
    64: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1",  # Gadolinium
    78: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9", # Platinum
    79: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10", # Gold
    89: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1", # Actinium
    90: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2", # Thorium
    91: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f2 6d1", # Protactinium
    92: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f3 6d1", # Uranium
    93: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4 6d1", # Neptunium
    94: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f6", # Plutonium
    95: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7", # Americium
    96: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7 6d1", # Curium
}

# Function to determine the maximum number of electrons in a subshell
def max_electrons(subshell):
    if 's' in subshell:
        return 2
    elif 'p' in subshell:
        return 6
    elif 'd' in subshell:
        return 10
    elif 'f' in subshell:
        return 14
    else:
        return 0

# exception handling of aufbau in case of half/full-filled orbitals
if atomic_no in exceptions:
    config = exceptions[atomic_no]
else:
    # non-exceptional aufbau elements
    for spdf in subshell:
        maxE = max_electrons(spdf)
        if atomic_no == 0:
            break
        elif atomic_no >= maxE:
            config += f"{spdf}{maxE} "
            atomic_no -= maxE
        else:
            config += f"{spdf}{atomic_no} "
            atomic_no = 0

print(config)
print("\nPlease note that certain elements may be exceptional to the aufbau principle. Almost ALL lanthanides"
      " are exceptions but only 21 have been accounted for, here.")
input("Press any key to exit...")
# akshat
