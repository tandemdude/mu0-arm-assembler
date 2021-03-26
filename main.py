import enum

ASSEMBLY_FILE = "assembly.txt"
MACHINE_CODE_FILE = "machine_code.txt"


class Opcodes(enum.IntEnum):
    LDA = 0x0
    STA = 0x1
    ADD = 0x2
    SUB = 0x3
    JMP = 0x4
    JMI = 0x5
    JEQ = 0x6
    STP = 0x7
    LDI = 0x8
    LSL = 0x9
    LSR = 0xA


def parts_to_machine_code(parts):
    if len(parts) < 2:
        return parts[0]
    return f"{hex(parts[0])}{parts[1]}"


def convert_line(line: str):
    parts = line.split()

    if parts[0].startswith("0"):
        return (parts[0],)
    return getattr(Opcodes, parts[0]), parts[1][2:] if len(parts) > 1 else "000"


if __name__ == "__main__":
    with open(ASSEMBLY_FILE) as fp:
        assembly = fp.read().split("\n")

    out = []
    for instruction in assembly:
        out.append(parts_to_machine_code(convert_line(instruction)))

    with open(MACHINE_CODE_FILE, "w") as fp:
        fp.write("\n".join(out))
