import os
import read_config

site_info = read_config.config.get("site_info")
commands = read_config.config.get("commands")
log_path = read_config.config.get("log_path")

def mobatch_tool(site_info,commands,log_path):
    os.system(f"mobatch {site_info} {commands} {log_path}")
    return log_path

if __name__ == '__main__':
    mobatch_tool(site_info,commands,log_path)