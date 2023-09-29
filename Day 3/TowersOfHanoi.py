def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1  # Return 1 for the single disk movement
    else:
        # Move n-1 disks from source to auxiliary using target as an auxiliary
        count1 = hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        # Move n-1 disks from auxiliary to target using source as an auxiliary
        count2 = hanoi(n - 1, auxiliary, source, target)
        # Total movements for n disks = movements for n-1 disks + 1 (current movement) + movements for n-1 disks
        return count1 + 1 + count2

n = int(input())
total_movements = hanoi(n, 'A', 'B', 'C')
print(f"Total movements for {n} disks: {total_movements}")
