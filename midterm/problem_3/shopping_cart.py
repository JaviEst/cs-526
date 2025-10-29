def shopping_cart(aisle: list[str]) -> str:
    """
    Determine the maximum number of items that can be collected using 2 baskets,
    where each basket can only hold one category of item.
    Starting from any aisle of choice, collect items from left to right.
    
    Args:
        aisle: List of category names representing items in aisles from left to right
        
    Returns:
        String indicating the maximum number of items that were selected
    """
    max_items = 0
    
    # Try starting from each possible position
    for start_idx in range(len(aisle)):
        basket_1: dict[str, int] = {}
        basket_2: dict[str, int] = {}
        items_collected = 0
        
        # Collect items from start_idx to the end
        for i in range(start_idx, len(aisle)):
            category = aisle[i]
            
            # Try to put item in basket 1 (if empty or already contains this category)
            if (not basket_1) or (category in basket_1):
                basket_1[category] = basket_1.get(category, 0) + 1
                items_collected += 1
            # Try to put item in basket 2 (if empty or already contains this category)
            elif (not basket_2) or (category in basket_2):
                basket_2[category] = basket_2.get(category, 0) + 1
                items_collected += 1
            # Cannot put item in either basket - must stop shopping
            else:
                break
        
        # Update maximum items collected
        max_items = max(max_items, items_collected)
    
    return f"{max_items} items were selected" 