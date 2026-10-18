def search_index_in_list(list: list[str], target: str) -> int:
    """
    Fetching the index of target if it is in the list
    """
    
    index = -1
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    
    return index