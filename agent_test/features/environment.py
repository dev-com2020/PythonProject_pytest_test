def before_scenario(context, scenario):
    print(f"Rozpoczynam scenariusz: {scenario.name}")


def after_scenario(context, scenario):
    print(f"Zakończono scenariusz: {scenario.name}")
