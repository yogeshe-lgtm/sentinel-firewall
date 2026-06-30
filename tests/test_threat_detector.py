from threat_detector import ThreatDetector

detector = ThreatDetector()

for port in range(1, 25):

    packet = {
        "source": "192.168.1.100",
        "destination": "192.168.1.1",
        "protocol": "TCP",
        "destination_port": port,
    }

    result = detector.analyze(packet)

print(result)
