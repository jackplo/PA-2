# Programming Assignment 2: Greedy Algorithms

## Authors

- Goran Not, UFID: 71994424
- Jack Lohse, UFID: 70686167

## Files

- 'main.py' => Entry point
- 'src/util/io.py' => File IO utility functions
- 'src/policies.py' => Actual implementations of FIFO, LRU, and OPTFF Caches.
- 'data/' => The directory containing the input and output data, output files are named exactly the same as input but with .out extension.
- 'PA-2 Questions.pdf' => The answers to the 3 questions in the written component

## Requirements/Dependencies

- Minimum Python >= 3.12 ('dict[int,int]' type hints used)
- Python package manager uv

## How to run

Clone the repo with:

```bash
git clone git@github.com:jackplo/PA-2.git
```

This project utilizes UV to make project management and package installation easier. This project can still be run without using uv, but it is highly recommended to use uv as it makes the process much easier. We outline the procedure for both methods below.

**If using uv:**

Install the python uv package manager if you do not have it. Below are the commands for mac, window, and linux. Alternatively visit the [uv repo](https://github.com/astral-sh/uv) for more information:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installing uv, create a new virtual environment from the project root using:

```bash
uv venv
```

Then run the project with the following commands:

```bash
uv run main.py data/<input_file_name>.in
```

**If not using uv:**

```bash
python main.py data/<input_file_name>.in
```

The above commands may differ for some people based on devices or python version. Command alternative to `python` are `python3` and `py`
