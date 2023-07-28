# Auto Config Digi Device Script
# Developed by Cade Weiskopf

from digidevice import config

cfg = config.load(writable=True)

print("\nSetting new name to CWTest1234")
cfg.set("system.name", "CWTest1234")

is_committed = cfg.commit()
print(f"committed {is_committed}")
print(f"Reading system name {cfg.get('system.name')}")

print(cfg.dump())