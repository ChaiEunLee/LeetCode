/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k){
    
    struct ListNode* first = head;
    struct ListNode* second = head;

    // 입력받는 k는 1부터 indexing이 돼서 
    // k-2까지 해야해서 k-1로 지정해야함
    for (int i=0; i<k-1;i++){
        first = first->next;
    }

    struct ListNode* tail = first;

    // tail을 끝으로 보내버림 -> second는 head에서 출발했기 때문에 length - k 만큼 이동한 위치에 있게 됨.
    // !tail->next 하면 답 틀림. != NULL을 써야함.
    while(tail->next != NULL){
        second = second->next;
        tail = tail->next;
    }

    int tmp = first->val;
    first->val = second->val;
    second->val = tmp;

    return head;   
    }