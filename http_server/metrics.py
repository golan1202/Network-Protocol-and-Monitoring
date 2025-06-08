from prometheus_client import Summary, Counter

REQUEST_TIME = Summary('response_time_seconds', 'Response time in seconds')
PACKETS_TOTAL = Counter('packets_total', 'Total packets processed', ['protocol'])
DROPPED_PACKETS = Counter('dropped_packets_total', 'Dropped packets due to simulation', ['protocol'])