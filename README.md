# Endpoint Coding Challenge

This repository contains a script for the endpoint directoy tree coding challenge. Follow the steps below to set up and run the script.

## Getting Started

### Prerequisites
- **Python**: Version 3.6 or later
- A terminal or command-line interface

### Clone the Repository
To get started, clone the repository into your chosen directory:

```bash
git clone https://github.com/arielaslutsky/endpoint-coding-challenge.git
```

### Clone the Repository
To get started, clone the repository into your chosen directory:

```bash
git clone https://github.com/arielaslutsky/endpoint-coding-challenge.git
```

### Input File
Create an input file in the same directory as the script. The input file must follow the format demonstrated in `sampleInput.txt`, which is included in the repository.

#### Example Input File:

```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST
```

### Running the script
Navigate into the project directory.  The input file should also be in the same directory.

Run the script replacing `sampleInput.txt` with your input file. If an output file is not specified the output can be viewed at `output.txt`
```bash
python directory.py sampleInput.txt
```

The output file name is an optional second parameter.  If you want to specify an output file run the script below replacing `sampleOutput.txt` with the preferred ouput file name.
```bash
python directory.py sampleInput.txt sampleOutput.txt
```
