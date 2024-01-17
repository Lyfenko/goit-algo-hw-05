import chardet
import timeit
from tabulate import tabulate
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def detect_encoding(file_path):
    # Detects the encoding of a file using chardet
    with open(file_path, "rb") as file:
        result = chardet.detect(file.read())
    return result["encoding"]


def read_file(file_path, encoding):
    # Reads the file with the specified encoding
    with open(file_path, "r", encoding=encoding) as file:
        content = file.read()
    return content


def measure_time(algorithm, text, pattern):
    # Measures the execution time of an algorithm
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time


if __name__ == "__main__":
    # Paths to your files
    file_path_article1 = "стаття 1.txt"
    file_path_article2 = "стаття 2.txt"

    # Detect encoding for each file
    encoding_article1 = detect_encoding(file_path_article1)
    encoding_article2 = detect_encoding(file_path_article2)

    # Read files using detected encodings
    article1 = read_file(file_path_article1, encoding_article1)
    article2 = read_file(file_path_article2, encoding_article2)

    # Display detected encodings
    print(f"Detected encoding for стаття 1.txt: {encoding_article1}")
    print(f"Detected encoding for стаття 2.txt: {encoding_article2}")

    # Generate real substrings for search (one that exists, and one imaginary)
    existing_pattern_article1 = "Метою роботи є виявлення найбільш популярних алгоритмів"
    fake_pattern_article1 = "Путін хуйло"

    existing_pattern_article2 = "Спосіб зберігання даних рекомендаційної системи"
    fake_pattern_article2 = "Україна понад усе"

    # Measure algorithms execution time
    results = []
    algorithms = [boyer_moore_search, kmp_search, rabin_karp_search]

    for search_algorithm in algorithms:  # Change the loop variable name
        time_existing_pattern1 = measure_time(
            search_algorithm, article1, existing_pattern_article1
        )
        time_fake_pattern1 = measure_time(search_algorithm, article1, fake_pattern_article1)

        time_existing_pattern2 = measure_time(
            search_algorithm, article2, existing_pattern_article2
        )
        time_fake_pattern2 = measure_time(search_algorithm, article2, fake_pattern_article2)

        results.append(
            [
                search_algorithm.__name__,  # Use the algorithm name in the result
                time_existing_pattern1,
                time_fake_pattern1,
                time_existing_pattern2,
                time_fake_pattern2,
            ]
        )

    # Display results in a tabular format
    headers = [
        "Алгоритм",
        "Час (стаття 1, існуючий)",
        "Час (стаття 1, вигаданий)",
        "Час (стаття 2, існуючий)",
        "Час (стаття 2, вигаданий)",
    ]
    print(tabulate(results, headers=headers, tablefmt="github"))

    # Determine the fastest algorithm for each text separately and overall
    fastest_algorithm_article1_existing = min(results, key=lambda x: x[1])[0]
    fastest_algorithm_article1_fake = min(results, key=lambda x: x[2])[0]
    fastest_algorithm_article2_existing = min(results, key=lambda x: x[3])[0]
    fastest_algorithm_article2_fake = min(results, key=lambda x: x[4])[0]

    fastest_algorithm_overall_existing = min(results, key=lambda x: (x[1] + x[3]) / 2)[0]
    fastest_algorithm_overall_fake = min(results, key=lambda x: (x[2] + x[4]) / 2)[0]

    # Display conclusions
    print("\nВисновки:")
    print(
        f"Найшвидший алгоритм для статті 1 (існуючий підрядок): {fastest_algorithm_article1_existing}"
    )
    print(
        f"Найшвидший алгоритм для статті 1 (вигаданий підрядок): {fastest_algorithm_article1_fake}"
    )
    print(
        f"Найшвидший алгоритм для статті 2 (існуючий підрядок): {fastest_algorithm_article2_existing}"
    )
    print(
        f"Найшвидший алгоритм для статті 2 (вигаданий підрядок): {fastest_algorithm_article2_fake}"
    )
    print(
        f"Найшвидший алгоритм загалом (існуючий підрядок): {fastest_algorithm_overall_existing}"
    )
    print(
        f"Найшвидший алгоритм загалом (вигаданий підрядок): {fastest_algorithm_overall_fake}"
    )
