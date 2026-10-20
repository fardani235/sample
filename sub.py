
import subprocess


def ping_host(host):
    command = f"ping -c 1 {host}"

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout


if __name__ == "__main__":
    hostname = input("Enter hostname: ")
    print(ping_host(hostname))
