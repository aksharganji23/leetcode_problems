/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    
    while (curr != NULL) {
        struct ListNode* nextNode = curr->next; // save next
        curr->next = prev;                      // reverse pointer
        prev = curr;                            // move prev
        curr = nextNode;                        // move curr
    }
    
    return prev; // new head
}
