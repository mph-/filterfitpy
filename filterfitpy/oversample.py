from scipy.signal import resample

def oversample(x, M=16, window='hamming'):
    """Oversample signal by factor `M`.  By default, a Hamming window
    is applied to the FFT of the signal before zero-padding."""
    
    xx = resample(x, len(x) * M, window=window)
    return xx
