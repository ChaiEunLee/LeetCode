/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* tail = dummy;

    // Until one of two lists reaches the end
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // Append the remaining elements from list1 or list2
    if (list1) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }

    struct ListNode* result = dummy->next;
    free(dummy); // Free the dummy node since it's no longer needed
    return result;
}
