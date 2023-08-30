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
        
        // 입력받는 k는 1부터 indexing이 돼서 
        // k-2까지 해야해서 k-1로 지정해야함

        // first가 k-1만큼 앞으로 이동
        for (int i=0; i<k-1;i++){
            first = first->next;
        }

        // tail이 k-1만큼 움직인 first와 같은 위치에서 출발
        ListNode* tail = first;

        // tail을 끝으로 보내버림 -> second는 head에서 출발했기 때문에 length - k 만큼 이동한 위치에 있게 됨.
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