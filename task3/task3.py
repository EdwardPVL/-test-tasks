import json
import sys

def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py <values.json> <tests.json> <report.json>")
        return
    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    with open(values_file_path, 'r') as values_file:
        values = json.load(values_file)

    with open(tests_file_path, 'r') as tests_file:
        tests = json.load(tests_file)

    results = {}
    for value in values.get("values", []):
        results[value["id"]] = value["value"]

    with open(report_file_path, 'w') as report_file:
        json.dump(tests, report_file)

    with open(report_file_path, 'r') as report_file:
        report = json.load(report_file)

    report["tests"] = parse_tests(report.get("tests", []), results)

    with open(report_file_path, 'w') as report_file:
        json.dump(report, report_file)

def parse_tests(tests, results):
    for test in tests:
        if "values" in test:
            test["values"] = parse_tests(test["values"], results)

        if "value" in test and "id" in test and test["id"] in results:
            test["value"] = results[test["id"]]

    return tests

if __name__ == "__main__":
    main()