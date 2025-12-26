def rsa_encrypt(m, n, e):
    return pow(m, e, n)

def cyclic_attack(n, e, start_message):
    print(f"Cyclic Attack starting from message {start_message}")
    seen = {}   
    m = start_message
    step = 0

    while m not in seen:
        seen[m] = step
        c = rsa_encrypt(m, n, e)
        print(f"Step {step}: {m} -> {c}")
        m = c
        step += 1

    # cycle detected
    cycle_start = seen[m]
    cycle_length = step - cycle_start
    print(f"\nCycle detected starting at step {cycle_start} with length {cycle_length}")
    print(f"Cycle values: {list(seen.keys())[cycle_start:]}")

p = 61
q = 53
n = p * q     
e = 17
start_message = 23

cyclic_attack(n, e, start_message)
