from packages.bank import stat as bs, logic as bl, export as be
from packages.crm import stat as cs, logic as cl, export as ce


def main():
    bs.stat()
    bl.add(123)
    bl.changes(321)
    bl.delete(453)
    bl.show()
    li = [1,23,4,1,33,432,543,55]
    be.export(li)

    print("part 2")
    cs.stat()
    cl.add(123)
    cl.changes(321)
    cl.delete(453)
    cl.show()
    li = [1,23,4,1,33,432,543,55]
    ce.export(li)
    

if __name__ == "__main__":
    print("main.py was started")
    main()
