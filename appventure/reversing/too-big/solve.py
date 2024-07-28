from os import stat
import angr
import claripy
import capstone
import logging

logging.getLogger("claripy.ast.bv").setLevel("ERROR")
logging.getLogger("angr.storage").setLevel("ERROR")
logging.getLogger("angr.simos").setLevel("ERROR")
logging.getLogger("angr.analyses.cfg").setLevel("ERROR")


def char(state, c):
    return state.solver.And(c <= "~", c >= " ")

INPUT_LENGTH = 56

p = angr.Project("{}".format("./chal"), auto_load_libs=False)

flag = claripy.BVS("flag", INPUT_LENGTH * 8)

state = p.factory.entry_state(stdin=flag)
state.options.add(angr.options.LAZY_SOLVES)

flag_format = b"AVCTF{"
for i,c in enumerate(flag.chop(8)):
    state.solver.add(char(state, c))
    if i < len(flag_format):
        state.solver.add(c == flag_format[i])


sm = p.factory.simulation_manager(state)
# Does not need to explore whole binary to obtain flag
sm.explore(find=0x4078E8)
print("finding...")

if sm.found:
    found = sm.found[0]
    solution = found.solver.eval(flag, cast_to=bytes)
    print("found: {}".format(solution))
else:
    print("not found")
    solution = None