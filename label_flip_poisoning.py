# Implement your attack code in this stub
def flip_labels(y, poison_percentage, seed):
    n_samples = len(y)
    n_to_flip = int(n_samples * poison_percentage)
    rng_instance = np.random.default_rng(seed)
    # Select unique indices to flip
    flipped_indices = rng_instance.choice(n_samples, size=n_to_flip, replace=False)

    y_poisoned = y.copy()

    # Get the original labels at the indices we are about to flip
    original_labels_at_flipped = y_poisoned[flipped_indices]

    # Apply the flip: if original was 0, set to 1; otherwise (if 1), set to 0
    y_poisoned[flipped_indices] = np.where(original_labels_at_flipped == 0, 1, 0)

    return y_poisoned, flipped_indices
