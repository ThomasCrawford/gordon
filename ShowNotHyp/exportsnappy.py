import snappy

M=snappy.Manifold('s782')

M.dehn_fill((-1,1),0)

M=M.identify()

print M._to_string()