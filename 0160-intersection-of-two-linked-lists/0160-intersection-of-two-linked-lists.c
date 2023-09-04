/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    if (!headA || !headB) {
        return NULL;
    }

    struct ListNode *rootA = headA;
    struct ListNode *rootB = headB;

    while (rootA != rootB) {
        rootA = rootA ? rootA->next : headB;
        rootB = rootB ? rootB->next : headA;
    }

    return rootA;
}