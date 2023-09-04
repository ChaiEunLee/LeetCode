/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head){
    // node가 1개 일 떄
    if (head->next == NULL){return NULL;}

    // slow->next가 없을 때 오류가 나지 않기 위해서 fast를 더 앞에서 시작함
    struct ListNode* slow = head;
    struct ListNode* fast = head->next->next;

    while (fast && fast->next){ // 이 조건이 중요!
        fast = fast->next->next;
        slow = slow->next;
    }
    slow -> next = slow->next->next;

    return head;
}
