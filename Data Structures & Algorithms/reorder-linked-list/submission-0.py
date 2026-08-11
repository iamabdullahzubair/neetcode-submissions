class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # --------------------------------------------------
        # Step 1: Find the middle of the linked list
        # --------------------------------------------------

        slow = head
        fast = head

        # slow moves 1 step
        # fast moves 2 steps
        # When fast reaches the end, slow is at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # --------------------------------------------------
        # Step 2: Split the linked list into two halves
        # --------------------------------------------------

        # 'slow' is the last node of the first half
        # The node after slow is the beginning of the second half
        second_half_head = slow.next

        # Break the connection between the two halves
        slow.next = None

        # Now we have:
        #
        # First half:  1 → 2 → 3
        # Second half: 4 → 5
        #
        # depending on the size of the original list

        # --------------------------------------------------
        # Step 3: Reverse the second half
        # --------------------------------------------------

        previous_node = None
        current_node = second_half_head

        while current_node:
            next_node = current_node.next

            # Reverse the current node's pointer
            current_node.next = previous_node

            # Move previous_node forward
            previous_node = current_node

            # Move current_node forward
            current_node = next_node

        # previous_node is now the head of the reversed
        # second half
        #
        # Example:
        #
        # Before:  4 → 5
        # After:   5 → 4
        #
        # previous_node → 5

        # --------------------------------------------------
        # Step 4: Merge both halves alternately
        # --------------------------------------------------

        first_half_current = head
        second_half_current = previous_node

        while first_half_current and second_half_current:

            # Save the next nodes before changing pointers
            first_half_next = first_half_current.next
            second_half_next = second_half_current.next

            # Connect one node from the second half
            # after the current node of the first half
            first_half_current.next = second_half_current

            # Connect the next first-half node after it
            second_half_current.next = first_half_next

            # Move to the next nodes of both halves
            first_half_current = first_half_next
            second_half_current = second_half_next
