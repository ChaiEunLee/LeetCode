/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) {
            return nullptr;
        }
        
        ListNode* rootA = headA;
        ListNode* rootB = headB;
        
        while (rootA != rootB) {
            rootA = rootA ? rootA->next : headB;
            rootB = rootB ? rootB->next : headA;
        }
        
        return rootA;
    }
};