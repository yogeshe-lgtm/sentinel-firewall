from src. rule_engine import RuleEngine



engine = RuleEngine()


packet = {

    "protocol":"TCP",

    "destination_port":22

}


result = engine.check_packet(packet)


print(result)
