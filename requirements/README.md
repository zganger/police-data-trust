The application can run in several different environments, each of which may have different dependency requirements. This directory generates `requirements.txt` files for each environment from template `*.in` files.

## Adding Requirements (Docker)

1. Add your requirements to `_core.in`, `dev_unix.in`, `prod_unix.in`, or `test_unix.in` as appropriate.

2. Update the `.txt` requirements files by running this command:

```bash
cd requirements
docker-compose up --build --force-recreate
```

3. Commit the updated `.txt` and `.in` files. Docker will install the requirements in the container, ensuring that the requirements are consistent across all environments.

## Adding Requirements (Native)
If you run the application natively, first install the pip-compile tool:

```bash
python -m ensurepip
python -m pip install pip-tools
```

Then generate the requirements:

```bash
python requirements/update.py
```

## Installing Requirements

Run the following command from the base of the repository:

```bash
# Optional, install pip if not already installed
python -m ensurepip

# Replace dev_unix with your environment
python -m pip install -r requirements/dev_unix.txt
```

> [!NOTE]  
> The requirements.txt files that are checked in should be generated using the docker command to ensure consistency.
