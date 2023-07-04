import os
import json

log_folder = "/solution/logs"
error_count = 0
for filename in os.listdir(log_folder):
    with open(os.path.join(log_folder, filename), "r") as file:
        for line in file:
            try:
                log_entry = json.loads(line)
                if (
                    log_entry["datetime"].startswith("22-08")
                    and log_entry.get("api_method")
                    and log_entry["api_method"].startswith("v2/")
                    and log_entry.get("status_code") == 500
                    and log_entry.get("host")
                    and log_entry["host"].endswith(".vla.yp-c.yandex.net")
                ):
                    error_count += 1
            except json.JSONDecodeError:
                continue

print(error_count)
