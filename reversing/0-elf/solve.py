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

INPUT_LENGTH = 33

p = angr.Project("{}".format("./chal"), auto_load_libs=False)

flag = claripy.BVS("flag", INPUT_LENGTH * 8)

state = p.factory.entry_state(stdin=flag)
state.options.add(angr.options.LAZY_SOLVES)

for i,c in enumerate(flag.chop(8)):
    state.solver.add(char(state, c))

sm = p.factory.simulation_manager(state)
sm.explore(find=0x4011dc, avoid=0x4011c4)
print("finding...")

if sm.found:
    found = sm.found[0]
    solution = found.solver.eval(flag, cast_to=bytes)
    print("found: {}".format(solution))
else:
    print("not found")
    solution = None