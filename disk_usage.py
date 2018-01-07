import os

def disk_usage(path):
    """Returns the immediate disk usage (measured in bytes) for the file or directory"""
    total = os.path.getsize(path)
    
    if os.path.isdir(path):
        
        for entry in os.listdir(path):
            entryPath = os.path.join(path, entry)
            total += disk_usage(entryPath)
    print('{0:<7}'.format(total), path)
    return total
