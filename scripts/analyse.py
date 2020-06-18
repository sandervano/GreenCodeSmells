import get_result
import plot_results
import detect_anomalies
import get_significance
import sys

path = sys.argv[1]

get_result.get_results(path, "norm_")
get_result.get_results(path, "smell_")

detect_anomalies.remove_anomalies(path, "norm_result")
detect_anomalies.remove_anomalies(path, "smell_result")

plot_results.plot_results(path)

get_significance.significance(path)
