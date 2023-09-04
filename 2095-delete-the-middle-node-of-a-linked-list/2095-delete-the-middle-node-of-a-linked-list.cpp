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
    ListNode* deleteMiddle(ListNode* head) {
        // node가 1개 일 때
        if (head->next == nullptr){return nullptr;} 

        // slow->next가 없을 때 오류가 나지 않기 위해서 fast를 더 앞에서 시작함
        ListNode* slow = head;
        ListNode* fast = head->next->next;

        while (fast and fast->next){ // 이 조건이 중요!
            fast = fast->next->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;

        return head;
    }
};