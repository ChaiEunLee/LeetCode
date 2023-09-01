/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    if (!head) {return head;}
    struct ListNode * lastElement = head;
    int length = 1;
    // list의 길이 / 마지막 node 구하기
    while (lastElement->next){
        lastElement = lastElement->next;
        length ++;
    }
    k = k % length; // k=length인 경우 0으로 만들어주기 위함
    lastElement->next = head; //마지막 node가 첫번째 노드를 가리킴 (circular로 만듬)
    struct ListNode * tempNode = head;
    for (int i=0; i<length-k-1;i++){
        tempNode = tempNode->next; // 마지막 node가 될 애를 구함
    }
    struct ListNode * answer = tempNode->next; // 첫번째 노드 지정
    tempNode->next = NULL; // 마지막 노드로 만들어버림
    return answer;
}