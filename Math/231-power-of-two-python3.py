class Solution:

    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1


# Main function
def main():

    # Input data
    n = 16

    # Create Solution object
    obj = Solution()

    # Function call
    result = obj.isPowerOfTwo(n)

    # Print output
    print("Input:", n)
    print("Is Power Of Two:", result)


if __name__ == "__main__":
    main()
