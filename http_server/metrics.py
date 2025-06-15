from prometheus_client import Summary, Counter, Histogram

PACKETS_TOTAL = Counter('packets_total', 'Total packets processed', ['protocol'])
DROPPED_PACKETS = Counter('dropped_packets_total', 'Dropped packets due to simulation', ['protocol'])
RESPONSE_TIME_SECONDS = Histogram("response_time_seconds","Response time in seconds",['protocol'])