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
    ListNode* reverseList(ListNode* head) {
        ListNode * prev = nullptr;
        ListNode * curNode = head;
        ListNode * next = nullptr;
        while (curNode != nullptr){
            next = curNode->next;
            curNode->next = prev;
            prev = curNode;
            curNode = next;
        }
        return prev;        
    }
};