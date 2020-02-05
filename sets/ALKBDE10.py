systems = {
    'bef' : { 'atoms' : ['Be', 'F'], 'coords' : [[0.0, 0.0, -0.6823625], [0.0, 0.0, 0.6823625]], 'charge' : 0, 'spin' : 1 },
    'cao' : { 'atoms' : ['Ca', 'O'], 'coords' : [[0.0, 0.0, -0.898729], [0.0, 0.0, 0.898729]], 'charge' : 0, 'spin' : 0 },
    'li' : { 'atoms' : ['Li'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 1 },
    'nao' : { 'atoms' : ['Na', 'O'], 'coords' : [[0.0, 0.0, -0.9755792], [0.0, 0.0, 0.9755792]], 'charge' : 0, 'spin' : 1 },
    'beo' : { 'atoms' : ['Be', 'O'], 'coords' : [[0.0, 0.0, -0.6586855], [0.0, 0.0, 0.6586855]], 'charge' : 0, 'spin' : 0 },
    'ca' : { 'atoms' : ['Ca'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 0 },
    'lif' : { 'atoms' : ['Li', 'F'], 'coords' : [[0.0, 0.0, 0.7824649], [0.0, 0.0, -0.7824649]], 'charge' : 0, 'spin' : 0 },
    'hf' : { 'atoms' : ['H', 'F'], 'coords' : [[0.0, 0.0, 0.4580069], [0.0, 0.0, -0.4580069]], 'charge' : 0, 'spin' : 0 },
    'h' : { 'atoms' : ['H'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 1 },
    'be' : { 'atoms' : ['Be'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 0 },
    'na' : { 'atoms' : ['Na'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 1 },
    'f' : { 'atoms' : ['F'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 1 },
    'lio' : { 'atoms' : ['Li', 'O'], 'coords' : [[0.0, 0.0, 0.7943231], [0.0, 0.0, -0.7943231]], 'charge' : 0, 'spin' : 1 },
    'mgo' : { 'atoms' : ['Mg', 'O'], 'coords' : [[0.0, 0.0, 0.8639034], [0.0, 0.0, -0.8639034]], 'charge' : 0, 'spin' : 0 },
    's' : { 'atoms' : ['S'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 2 },
    'mg' : { 'atoms' : ['Mg'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 0 },
    'kf' : { 'atoms' : ['K', 'F'], 'coords' : [[0.0, 0.0, -1.088871], [0.0, 0.0, 1.088871]], 'charge' : 0, 'spin' : 0 },
    'o' : { 'atoms' : ['O'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 2 },
    'k' : { 'atoms' : ['K'], 'coords' : [[0.0, 0.0, 0.0]], 'charge' : 0, 'spin' : 1 },
    'mgs' : { 'atoms' : ['Mg', 'S'], 'coords' : [[0.0, 0.0, -1.0662361], [0.0, 0.0, 1.0662361]], 'charge' : 0, 'spin' : 0 },
}

reactions = [
    { 'systems' : ['bef', 'be', 'f'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 138.700000 },
    { 'systems' : ['beo', 'be', 'o'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 106.600000 },
    { 'systems' : ['cao', 'ca', 'o'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 96.200000 },
    { 'systems' : ['hf', 'h', 'f'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 142.100000 },
    { 'systems' : ['kf', 'k', 'f'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 117.500000 },
    { 'systems' : ['lif', 'li', 'f'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 139.200000 },
    { 'systems' : ['lio', 'li', 'o'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 82.500000 },
    { 'systems' : ['mgo', 'mg', 'o'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 62.200000 },
    { 'systems' : ['mgs', 'mg', 's'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 56.700000 },
    { 'systems' : ['nao', 'na', 'o'], 'stoichiometry' : ['-1', '1', '1'], 'reference' : 65.200000 },
]
