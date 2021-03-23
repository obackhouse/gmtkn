from sets import W4_11, \
                 G21EA, \
                 G21IP, \
                 DIPCS10, \
                 PA26, \
                 SIE4x4, \
                 ALKBDE10, \
                 YBDE18, \
                 AL2X6, \
                 HEAVYSB11, \
                 NBPRC, \
                 ALK8, \
                 RC21, \
                 G2RC, \
                 FH51, \
                 TAUT15, \
                 DC13, \
                 MB16_43, \
                 DARC, \
                 RSE43, \
                 BSR36, \
                 CDIE20, \
                 ISO34, \
                 ISOL24, \
                 C60ISO, \
                 PArel, \
                 BH76, \
                 BHPERI, \
                 BHDIV10, \
                 INV24, \
                 BHROT27, \
                 PX13, \
                 WCPT18, \
                 RG18, \
                 ADIM6, \
                 S22, \
                 S66, \
                 HEAVY28, \
                 WATER27, \
                 CARBHB12, \
                 PNICO23, \
                 HAL59, \
                 AHB21, \
                 CHB6, \
                 IL16, \
                 IDISP, \
                 ICONF, \
                 ACONF, \
                 Amino20x4, \
                 PCONF21, \
                 MCONF, \
                 SCONF, \
                 UPU23, \
                 BUT14DIOL, \
                 GW100, \
                 GAPS

sets = { 'W4_11'     : W4_11, \
         'G21EA'     : G21EA, \
         'G21IP'     : G21IP, \
         'DIPCS10'   : DIPCS10, \
         'PA26'      : PA26, \
         'SIE4x4'    : SIE4x4, \
         'ALKBDE10'  : ALKBDE10, \
         'YBDE18'    : YBDE18, \
         'AL2X6'     : AL2X6, \
         'HEAVYSB11' : HEAVYSB11, \
         'NBPRC'     : NBPRC, \
         'ALK8'      : ALK8, \
         'RC21'      : RC21, \
         'G2RC'      : G2RC, \
         'FH51'      : FH51, \
         'TAUT15'    : TAUT15, \
         'DC13'      : DC13, \
         'MB16_43'   : MB16_43, \
         'DARC'      : DARC, \
         'RSE43'     : RSE43, \
         'BSR36'     : BSR36, \
         'CDIE20'    : CDIE20, \
         'ISO34'     : ISO34, \
         'ISOL24'    : ISOL24, \
         'C60ISO'    : C60ISO, \
         'PArel'     : PArel, \
         'BH76'      : BH76, \
         'BHPERI'    : BHPERI, \
         'BHDIV10'   : BHDIV10, \
         'INV24'     : INV24, \
         'BHROT27'   : BHROT27, \
         'PX13'      : PX13, \
         'WCPT18'    : WCPT18, \
         'RG18'      : RG18, \
         'ADIM6'     : ADIM6, \
         'S22'       : S22, \
         'S66'       : S66, \
         'HEAVY28'   : HEAVY28, \
         'WATER27'   : WATER27, \
         'CARBHB12'  : CARBHB12, \
         'PNICO23'   : PNICO23, \
         'HAL59'     : HAL59, \
         'AHB21'     : AHB21, \
         'CHB6'      : CHB6, \
         'IL16'      : IL16, \
         'IDISP'     : IDISP, \
         'ICONF'     : ICONF, \
         'ACONF'     : ACONF, \
         'Amino20x4' : Amino20x4, \
         'PCONF21'   : PCONF21, \
         'MCONF'     : MCONF, \
         'SCONF'     : SCONF, \
         'UPU23'     : UPU23, \
         'BUT14DIOL' : BUT14DIOL, \
         'GW100'     : GW100, \
         'GAPS'      : GAPS,
}

def __getattr__(key):
    '''
    Searches the module for a particular key. Order of operations:

        1. Check if key is a named test set, if so, return the set

        2. Check if key is a named system in the W4-11 set, if so,
           return the system

        3. Check if key is a named system in any other set, with
           sets checked alphabetically

        4. Else, raise an error.
    '''


    # 1.
    if key in sets:
        return sets[key]

    # 2.
    if key in sets['W4_11'].systems:
        return sets['W4_11'].systems[key]

    # 3.
    for name in sorted(sets.keys()):
        if key in sets[name].systems:
            return sets[name].systems[key]

    # 4.
    raise IndexError('Could not find item %s in gmtkn module.' % key)
