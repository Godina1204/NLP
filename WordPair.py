def edit_distance(source, target, sub_cost=1, ins_cost=1, del_cost=1):
    m, n = len(source), len(target)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Initialize base cases
    for i in range(m+1):
        dp[i][0] = i * del_cost
    for j in range(n+1):
        dp[0][j] = j * ins_cost

    # Fill DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j-1] + sub_cost,  # substitution
                    dp[i][j-1] + ins_cost,    # insertion
                    dp[i-1][j] + del_cost     # deletion
                )

    return dp[m][n], dp

def reconstruct_path(dp, source, target, sub_cost=1, ins_cost=1, del_cost=1):
    i, j = len(source), len(target)
    edits = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and source[i-1] == target[j-1]:
            edits.append(f"Keep '{source[i-1]}'")
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + sub_cost:
            edits.append(f"Substitute '{source[i-1]}' → '{target[j-1]}'")
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + ins_cost:
            edits.append(f"Insert '{target[j-1]}'")
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + del_cost:
            edits.append(f"Delete '{source[i-1]}'")
            i -= 1

    return edits[::-1]

# Inputs
source = "Sunday"
target = "Saturday"

# Model A
dist_a, dp_a = edit_distance(source, target, sub_cost=1, ins_cost=1, del_cost=1)
path_a = reconstruct_path(dp_a, source, target, sub_cost=1, ins_cost=1, del_cost=1)

# Model B
dist_b, dp_b = edit_distance(source, target, sub_cost=2, ins_cost=1, del_cost=1)
path_b = reconstruct_path(dp_b, source, target, sub_cost=2, ins_cost=1, del_cost=1)

# Output
print("Model A (Sub=1, Ins=1, Del=1):")
print("Minimum Edit Distance:", dist_a)
print("Edit Sequence:")
for step in path_a:
    print(" -", step)

print("\nModel B (Sub=2, Ins=1, Del=1):")
print("Minimum Edit Distance:", dist_b)
print("Edit Sequence:")
for step in path_b:
    print(" -", step)
