import requests
import time
import copy

def download_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Failed to download text from {url}: {e}")
        return None

def load_text(article_url, cached_texts):
    if article_url in cached_texts:
        return cached_texts[article_url]
    else:
        text = download_text(article_url)
        cached_texts[article_url] = text
        return text

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1

    last_occurrence = {}
    for i, char in enumerate(pattern):
        last_occurrence[char] = i

    i = m - 1
    while i < n:
        k = i
        j = m - 1
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j == -1:
            return k + 1
        if text[i] not in last_occurrence:
            i += m
        else:
            i += max(1, j - last_occurrence[text[i]])
    return -1

def knuth_morris_pratt(text, pattern):
    def build_failure_function(pattern):
        m = len(pattern)
        failure = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[j] != pattern[i]:
                j = failure[j - 1]
            if pattern[j] == pattern[i]:
                j += 1
            failure[i] = j
        return failure

    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1

    failure = build_failure_function(pattern)
    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = failure[j - 1]
        if pattern[j] == text[i]:
            j += 1
            if j == m:
                return i - m + 1

    return -1

def rabin_karp(text, pattern):
    def rabin_fingerprint(s, m):
        result = 0
        BASE = 256
        MOD = 101
        for i in range(m):
            result = (result * BASE + ord(s[i])) % MOD
        return result

    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1

    def update_fingerprint(fingerprint, old_char, new_char, m):
        BASE = 256
        MOD = 101
        return ((fingerprint - ord(old_char) * pow(BASE, m - 1, MOD)) * BASE + ord(new_char)) % MOD

    pattern_hash = rabin_fingerprint(pattern, m)
    text_hash = rabin_fingerprint(text[:m], m)
    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i+m] == pattern:
            return i
        if i < n - m:
            text_hash = update_fingerprint(text_hash, text[i], text[i + m], m)
            if text_hash < 0:
                text_hash += 101

    return -1

def measure_algorithm_performance(text, pattern, algorithms):
    text_copy = copy.deepcopy(text)
    for algorithm_name, algorithm in algorithms.items():
        print(f"Performance for {algorithm_name}:")
        start_time = time.time()
        algorithm_result = algorithm(text_copy, pattern)
        end_time = time.time()
        print(f"    Time taken: {end_time - start_time} seconds")
        if algorithm_result == -1:
            print("    Pattern not found.")

def main():
    cached_texts = {}

    article1_url = "https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
    article2_url = "https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"

    article1_text = load_text(article1_url, cached_texts)
    article2_text = load_text(article2_url, cached_texts)

    if article1_text and article2_text:
        print("Texts downloaded successfully.")
    else:
        print("Failed to download one or both texts.")
        return

    existing_pattern = "структури даних"
    non_existing_pattern = "структури всіх даних"

    algorithms = {
        "Boyer-Moore": boyer_moore,
        "Knuth-Morris-Pratt": knuth_morris_pratt,
        "Rabin-Karp": rabin_karp
    }

    print("Performance for existing pattern in article 1:")
    measure_algorithm_performance(article1_text, existing_pattern, algorithms)
    
    print("Performance for non-existing pattern in article 1:")
    measure_algorithm_performance(article1_text, non_existing_pattern, algorithms)

    print("Performance for existing pattern in article 2:")
    measure_algorithm_performance(article2_text, existing_pattern, algorithms)
    
    print("Performance for non-existing pattern in article 2:")
    measure_algorithm_performance(article2_text, non_existing_pattern, algorithms)

if __name__ == "__main__":
    main()