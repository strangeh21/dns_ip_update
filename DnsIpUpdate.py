import requests
import schedule
import datetime
import time


def main():
    dns_ip_update = DnsIpUpdate()
    dns_ip_update.update_dns_ip()
    schedule.every(5).minutes.do(dns_ip_update.update_dns_ip)
    while True:
        try:
            schedule.run_pending()
            time.sleep(30)
        except Exception as e:
            print("Your process crashed. Restarting in 60 seconds.")
            print(f"error e: {e} || e.args: {e.args} || type(e): {type(e)}")
            time.sleep(60)
            pass


class DnsIpUpdate:
    # Add the sync URLs below and the domain.
    updates = [
        ("website.example", "http://exampledomain.example/u/xxxx/"),
        ("website2.example", "http://exampledomain.example/u/xxxx/"),
        ("website3.example", "http://exampledomain.example/u/xxxx/"),
    ]

    @staticmethod
    def update_dns_ip():
        start_time = datetime.datetime.now()
        print(f"Attempting to update DNS records as of: {start_time}")
        ip = DnsIpUpdate.get_ip()
        if ip is None:
            pass
        for domain, url in DnsIpUpdate.updates:
            response = None
            try:
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                if response.status_code == 200:
                    print(f"Updated: {domain} to IP: {ip}")
                else:
                    raise Exception
            except Exception as e:
                print(f"Error for domain: {domain} || ", end="")
                print(f"Status: {response.status_code} || ", end="")
                print(f"error: {e} || type(e): {type(e)} || e.args: {e.args}")
        print(f"Finished updating DNS records in: {datetime.datetime.now() - start_time}")

    @staticmethod
    def get_ip():
        response = requests.get("http://ip-api.com/json/?fields=61439", timeout=3)
        if response.status_code == 200:
            return response.json()["query"]
        else:
            print(f"Error obtaining own IP. Status code: {response.status_code}")
            return None


if __name__ == "__main__":
    main()
