import sets as _sets

sets = { 'W4_11'     : _sets.W4_11, \
         'G21EA'     : _sets.G21EA, \
         'G21IP'     : _sets.G21IP, \
         'DIPCS10'   : _sets.DIPCS10, \
         'PA26'      : _sets.PA26, \
         'SIE4x4'    : _sets.SIE4x4, \
         'ALKBDE10'  : _sets.ALKBDE10, \
         'YBDE18'    : _sets.YBDE18, \
         'AL2X6'     : _sets.AL2X6, \
         'HEAVYSB11' : _sets.HEAVYSB11, \
         'NBPRC'     : _sets.NBPRC, \
         'ALK8'      : _sets.ALK8, \
         'RC21'      : _sets.RC21, \
         'G2RC'      : _sets.G2RC, \
         'FH51'      : _sets.FH51, \
         'TAUT15'    : _sets.TAUT15, \
         'DC13'      : _sets.DC13, \
         'MB16_43'   : _sets.MB16_43, \
         'DARC'      : _sets.DARC, \
         'RSE43'     : _sets.RSE43, \
         'BSR36'     : _sets.BSR36, \
         'CDIE20'    : _sets.CDIE20, \
         'ISO34'     : _sets.ISO34, \
         'ISOL24'    : _sets.ISOL24, \
         'C60ISO'    : _sets.C60ISO, \
         'PArel'     : _sets.PArel, \
         'BH76'      : _sets.BH76, \
         'BHPERI'    : _sets.BHPERI, \
         'BHDIV10'   : _sets.BHDIV10, \
         'INV24'     : _sets.INV24, \
         'BHROT27'   : _sets.BHROT27, \
         'PX13'      : _sets.PX13, \
         'WCPT18'    : _sets.WCPT18, \
         'RG18'      : _sets.RG18, \
         'ADIM6'     : _sets.ADIM6, \
         'S22'       : _sets.S22, \
         'S66'       : _sets.S66, \
         'HEAVY28'   : _sets.HEAVY28, \
         'WATER27'   : _sets.WATER27, \
         'CARBHB12'  : _sets.CARBHB12, \
         'PNICO23'   : _sets.PNICO23, \
         'HAL59'     : _sets.HAL59, \
         'AHB21'     : _sets.AHB21, \
         'CHB6'      : _sets.CHB6, \
         'IL16'      : _sets.IL16, \
         'IDISP'     : _sets.IDISP, \
         'ICONF'     : _sets.ICONF, \
         'ACONF'     : _sets.ACONF, \
         'Amino20x4' : _sets.Amino20x4, \
         'PCONF21'   : _sets.PCONF21, \
         'MCONF'     : _sets.MCONF, \
         'SCONF'     : _sets.SCONF, \
         'UPU23'     : _sets.UPU23, \
         'BUT14DIOL' : _sets.BUT14DIOL, \
         'GW100'     : _sets.GW100, \
         'GAPS'      : _sets.GAPS, \
         'MRADC'     : _sets.MRADC, \
         'ACC24'     : _sets.ACC24, \
         'S30L'      : _sets.S30L,
}

def __getattr__(key):
    '''
    Searches the module for a particular key. Order of operations:

        1. Check if key is a named test set, if so, return the set

        2. Check if key is a named system in the W4-11 set, if so,
           return the system

        3. Check if key is a named system in any other set except
           for GAPS, with sets checked alphabetically

        4. Else, raise an error.
    '''


    # 1.
    if key in sets:
        return sets[key].systems

    # 2.
    if key in sets['W4_11'].systems:
        return sets['W4_11'].systems[key]

    # 3.
    for name in sorted(sets.keys()):
        if name != 'GAPS':
            if key in sets[name].systems:
                return sets[name].systems[key]

    # 4.
    raise IndexError('Could not find item %s in gmtkn module.' % key)
