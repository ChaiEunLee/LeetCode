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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* first = head;
        ListNode* second = head;
        
        for (int i=0; i<k-1;i++){
            first = first->next;
        }
        ListNode* tail = first;
        while(tail->next != nullptr){
            second = second->next;
            tail = tail->next;
        }

        int tmp = first->val;
        first->val = second->val;
        second->val = tmp;

        return head;   
    }
};