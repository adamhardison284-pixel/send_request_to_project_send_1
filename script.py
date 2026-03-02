import requests
import time

URL = "https://wjbczrcovyoolwrnnmpg.supabase.co/functions/v1/PojectSend"

INTERVAL = 2          # seconds between requests
RUN_DURATION = 300    # run for 5 minutes


def trigger_process_emails(worker_id):
    try:
        response = requests.post(
            URL,
            json={
                "source": "github_cron",
                "cron_id": worker_id
            },
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        if response.status_code != 200:
            print(f"HTTP {response.status_code}: {response.text}")
            return None

        print("Success:", response.text)
        return response.text

    except Exception as e:
        print("Error triggering process:", e)
        return None


def main():
    inc = 0
    total_runs = RUN_DURATION // INTERVAL

    for _ in range(total_runs):
        inc += 1
        worker_id = f"{inc}test_5"
        trigger_process_emails(worker_id)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
