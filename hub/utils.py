import subprocess

from urllib.parse import urlparse


def process_run(run):
    try:
        # Set status to running
        run.status = 'running'
        run.save()

        # Extract repository details
        repo_url = run.cash_flow_model.repository_url
        repo_name = urlparse(repo_url).path.split('/')[-1].replace('.git', '')

        # Run commands
        commands = [
            f"git clone {repo_url}",
            f"cd {repo_name} && python run.py"
        ]
        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

        run.status = 'completed' if result.returncode == 0 else 'error'

    except Exception as e:
        run.status = 'error'
        print(f"Error processing run {run.id}: {e}")

    finally:
        run.save()
