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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr){return head;}
        ListNode * lastElement = head;
        int length = 1;
        // list의 길이 / 마지막 node 구하기
        while(lastElement->next != nullptr){
            lastElement = lastElement->next;
            length ++;
        }
        k = k % length; // k=length인 경우 0으로 만들어주기 위함
        lastElement->next = head; //마지막 node가 첫번째 노드를 가리킴 (circular로 만듬)
        ListNode * tempNode = head;
        for (int i=0; i<length-k-1;i++){
            tempNode = tempNode->next; // 마지막 node가 될 애를 구함
        }
        ListNode * answer = tempNode->next; // 첫번째 노드 지정
        tempNode->next = nullptr; // 마지막 노드로 만들어버림
        return answer;
    }
};