from collections import deque

def min_mutation(start_gene: str, end_gene: str, bank: list[str]) -> int:
    """Return minimum mutations from start_gene to end_gene via bank, or -1."""
    bank_set = set(bank)
    if end_gene not in bank_set:
        return -1
    
    queue = deque([(start_gene, 0)])
    visited = {start_gene}
    gene_chars = ['A', 'C', 'G', 'T']
    
    while queue:
        curr, depth = queue.popleft()
        if curr == end_gene:
            return depth
        
        for i in range(len(curr)):
            original_char = curr[i]
            for c in gene_chars:
                if c == original_char:
                    continue
                neighbor = curr[:i] + c + curr[i+1:]
                if neighbor in bank_set and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
    return -1
