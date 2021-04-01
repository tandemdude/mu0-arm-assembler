# Simple program to convert Mu0 assembly language to hexadecimal machine code

I wrote this small program because I was too lazy to manually convert a sequence of assembly instructions
into the appropriate machine code counterpart. This probably took more time to write than it would have
taken to convert the assembly manually but here we are.

## Usage

Populate `assembly.txt` with your assembly language, for example:

```
LDI 0x123
LDA 0x000
STA 0x102
LSR
ADD 0x002
SUB 0x002
LDA 0x102
```

Run the script `main.py`

A file - `machine_code.txt` will be created/overwritten with the hex machine code for the assembly language
you input.

Example:

```
0x8123
0x0000
0x1102
0xa000
0x2002
0x3002
0x0102
```
