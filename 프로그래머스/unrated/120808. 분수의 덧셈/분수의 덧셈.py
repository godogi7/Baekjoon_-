def solution(numer1, denom1, numer2, denom2):
    result_numer = numer1 * denom2 + numer2 * denom1
    result_denom = denom1 * denom2

    common_factor = gcd(result_numer, result_denom)
    result_numer //= common_factor
    result_denom //= common_factor    

    return [result_numer, result_denom]
def gcd(a,b):
    while b:
        a,b = b, a % b
    return a