/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode * prev = NULL;
    struct ListNode * curNode = head;
    struct ListNode * next = NULL;
    while (curNode != NULL){
        next = curNode->next;
        curNode->next = prev;
        prev = curNode;
        curNode = next;
    }
    return prev;        
}   
