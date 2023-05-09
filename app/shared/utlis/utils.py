from difflib import SequenceMatcher

def check_substring_list(text: str, items: set):
    if any(text in s for s in items):
        return True
    elif any(s in text for s in items):
        return True
    elif any(SequenceMatcher(None, text, s).ratio() > 0.8 for s in items):
        return True
    else:
        return False
    
def chunked_reader(f, chunksize=2 ** 20):  # 1Mb chunks
    while True:
        chunk = f.read(chunksize)
        if not chunk:
            return
        yield chunk