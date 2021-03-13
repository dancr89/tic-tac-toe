def rec_sums(n):
    if n == 0:
        return 0, 0, 0

    total_sum, even_sum, odd_sum = rec_sums(n - 1)

    total_sum += n

    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

    return total_sum, even_sum, odd_sum

total_sum, even_sum, odd_sum = rec_sums(10)

print('total_sum = ', total_sum)
print('even_sum = ', even_sum)
print('odd_sum = ', odd_sum)