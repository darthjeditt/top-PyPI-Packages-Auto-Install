# Top PyPI Packages Installer

This script fetches the top 50 most-downloaded Python packages from [hugovk's top-pypi-packages website](https://hugovk.github.io/top-pypi-packages/) and installs them in a new virtual environment.

## Prerequisites

- Python 3.x
- `requests` and `beautifulsoup4` libraries. You can install them using:
  ```bash
  pip install requests beautifulsoup4
  ```

## Usage

1. Clone this repository or download the script.
2. Navigate to the directory containing the script.
3. Run the script:
   ```bash
   python main.py
   ```
4. The script will create a new virtual environment named `topPackagesEnv` and install the top 50 packages in it.

## Activating the Virtual Environment

After running the script, you can activate the virtual environment:

- On Linux/macOS:
  ```bash
  source top_packages_venv/bin/activate
  ```

- On Windows:
  ```bash
  .\top_packages_venv\Scripts\activate
  ```

Remember to deactivate the virtual environment when you're done:

```bash
deactivate
```

## License

This project is open-sourced under the MIT License. See the LICENSE file for details.
