# BatchShield Decryptor Tool

![]()

The **BatchShield Decryptor Tool** allows you to make readable batch scripts that have been obfuscated using [BatchShield](https://github.com/DevBubba/BatchShield).

## Requirements

- Python 3.x

## Installation

Clone this repository:

```git clone https://github.com/Einstein2150/BatchShield-Decryptor```

Change into the directory:

```cd BatchShieldDecryptor```

<div style="border: 2px solid black; padding: 10px; display: inline-block;">
    <img src="pictures/MAIN.PNG" alt="MAIN" style="max-width: 100%;">
</div>
   	
## Usage

To deobfuscate a batch script, run the deobfuscator.py file with Python 3:

```python3 deobfuscator.py```

###Example

When the program runs, you will be prompted to enter the path to the obfuscated batch file (.bat) and the output file name for the deobfuscated content.

Enter the path to the obfuscated file and choose a name for the output file.

```Enter the path to the obfuscated batch file (.bat): obfuscated_script.bat```

```Enter the output file name for the deobfuscated content (.bat): deobfuscated_script.bat```

The program will remove all strings between percent signs (%) that were randomly obfuscated and save the deobfuscated content in the specified output file.
	