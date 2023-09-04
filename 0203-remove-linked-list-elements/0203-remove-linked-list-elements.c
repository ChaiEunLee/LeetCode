/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode * dummy = (struct ListNode*)malloc(sizeof(struct ListNode)); // C는 malloc으로 새로운 노드 만들어야함.
    struct ListNode * cur = dummy;
        dummy->next = head;
        
        while (cur->next){
            if (cur->next->val == val){cur->next = cur->next->next;}
            else {cur = cur->next;}
        } 
        return dummy->next;
}