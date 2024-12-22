import subprocess

from urllib.parse import urlparse


def parse_string_to_list(input_string):
    """
    Parse a string to convert it into a list of integers, expanding ranges defined by ':' or '-'.

    Args:
        input_string (str): Input string containing integers and ranges.

    Returns:
        list: A list of integers parsed from the input string.
    """
    result = []
    elements = input_string.split(',')  # Split by commas to get individual parts

    for element in elements:
        element = element.strip()  # Remove any surrounding whitespace

        if ':' in element or '-' in element:
            # Handle ranges defined by ':' or '-'
            start, end = map(int, element.replace(':', '-').split('-'))
            result.extend(range(start, end + 1))
        else:
            # Handle single numbers
            result.append(int(element))

    return result


def get_commands(run):
    # Extract repository details
    repo_url = run.cash_flow_model.repository_url
    repo_name = urlparse(repo_url).path.split('/')[-1].replace('.git', '')

    # Run commands
    if not run.version:
        run_commands = f"cd {repo_name} && python run.py"
    else:
        versions = parse_string_to_list(run.version)
        run_commands = []
        for version in versions:
            run_commands.append(f"cd {repo_name} && python run.py --version {version}")

    # Execution commands
    commands = [
        f"git clone {repo_url}",
        f"pip install cashflower",
    ]
    commands += run_commands
    return commands


def process_run(run):
    try:
        run.status = 'running'
        run.save()

        commands = get_commands(run)
        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

        run.status = 'completed' if result.returncode == 0 else 'error'

    except Exception as e:
        run.status = 'error'
        print(f"Error processing run {run.id}: {e}")

    finally:
        run.save()
