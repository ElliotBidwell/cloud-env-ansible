# This script runs the iPerf3 benchmark

import os
import subprocess

result_log_cli = "iperf_server.log"

def run_iperf_server():
    print("Running iPerf as server")
    subprocess.run(["iperf3", "-s", "-1"], check=True)
    result(f'//home/coremark/{result_log_serv}')
    print(f'Printed iPerf3 server benchmark results to {result_log_serv}')

run_iperf_server()
