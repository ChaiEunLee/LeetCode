/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode * dummy = new ListNode(0); // cpp에서는 new를 붙여서 새로운 노드를 만들어야함
        ListNode * cur = dummy;

        dummy->next = head;

        while (cur->next){
            if (cur->next->val == val){cur->next = cur->next->next;}
            else {cur = cur->next;}
        } 
        return dummy->next;
    }
};