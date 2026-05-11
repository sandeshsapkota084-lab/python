ab='rm'
ba=ab.replace('r','ra')
print(ba)

a = 'ram'
trans_table = str.maketrans({'r': 'R', 'a': 'A', 'm': 'M'})
b = a.translate(trans_table)
print(b)

inpu='ram'
output=inpu.maketrans('ram','api')
print(inpu.translate(output))

fn='   Laxmi    Prasad    Devkota   '
a=fn.strip()
b=a.replace('    ','_')
print(b)

c=fn.strip()
r="_".join(c.split())
print(r)