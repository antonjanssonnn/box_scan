import sys
import subprocess

IMAGE_NAME = "localhost/clamav_with_curl:latest"
VIRUS_SCAN_CONTAINER = "virus_scan_container"


def download_and_scan_file(url):
    """We start a container, download file and scan it"""
    try:
        print(f"🛡 Starting container and download file on {url}")

        result = subprocess.run(
            [
                "podman",
                "run",
                "--rm",
                "--name",
                VIRUS_SCAN_CONTAINER,
                IMAGE_NAME,
                "/bin/sh",
                "-c",
                f"curl -o /tmp/downloaded_file {url} && clamscan -r /tmp/downloaded_file",
            ],
            capture_output=True,
            text=True,
        )
        
        print(result.stdout)
        infected_files = []
        
        for line in result.stdout.split("\n"):
            if "FOUND" in line: 
                infected_files.append(line)
        
        if infected_files:
            print("⚠ Infected files detected:")
            for file_info in infected_files:
                print(f"🔴 {file_info}")
            
        else:
            print("✅ File is safe, do you want to extract it to your computer (y/n)")
            choice = input().strip().lower()
            if choice == "y":
                extract_file(url)
            
    except Exception as e:
        print(f"Error occured {e}")
        sys.exit(1)

def extract_file(url):
    """If the file is safe, we extract it to host computer"""
    
    filename = url.split("/")[-1]
    
    print("Saving file to host computer")
    
    subprocess.run(
        [
            "podman", "run", "--rm",
            "-v", f"{filename}:/output/{filename}:Z",
            IMAGE_NAME, "/bin/sh", "-c",
            f"cp /tmp/downloaded_file /output/{filename}"
        ]
    )
    print(f"File is stored as {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using: python download.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    download_and_scan_file(url)
