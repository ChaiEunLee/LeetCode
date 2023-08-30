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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next){return head;}

        ListNode* dummyNode = new ListNode(); // sentinel 만들기

        ListNode* prevNode = dummyNode;
        ListNode* currNode = head;

        // curNode.next <-> curNode를 swap 하는 것
        // swap : 1)node1 앞으로 자리 옮기고, 2)node2 뒤로 자리 옮기고, 3)node1-node2 연결하는 순서
        // 1) 앞 node(prevNode)와 연결 2) 뒤 node(prevNode->next->next)와 연결 3)연결
        while (currNode && currNode->next){
            prevNode->next = currNode->next; // currNode->next를 prevNode->next로 만들어서 curNode->next가 curNode 자리로 이동
            currNode->next = prevNode->next->next; // curNode->next 자리에다가 prevNode->next->next를 넣어서 curNode를 뒤로 보냄
            prevNode->next->next = currNode; // curNode를 앞에 있던 curNode.next와 연결

            prevNode = currNode;
            currNode = currNode->next;
        }
        return dummyNode->next;
    }
};