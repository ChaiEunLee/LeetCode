/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2);

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    if (listsSize == 0) {
        return NULL;
    }

    struct ListNode** list_ = (struct ListNode**)malloc(listsSize * sizeof(struct ListNode*));
    for (int i = 0; i < listsSize; ++i) {
        list_[i] = lists[i];
    }

    for (int i = 1; i < listsSize; ++i) {
        struct ListNode* x = mergeTwoLists(list_[i - 1], list_[i]);
        list_[i] = x;
    }

    struct ListNode* result = list_[listsSize - 1];
    free(list_);
    return result;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode * dummy = (struct ListNode*)malloc(sizeof(struct ListNode)); // C는 malloc으로 새로운 노드 만들어야함.
    struct ListNode * tail = dummy;

        // Until one of two list reached end
        while (list1 && list2){
            // Compare two values all the time
            if (list1->val >= list2->val){
                tail->next = list2;
                // Move on to next node
                //list2, tail = list2->next, list2;
                list2 = list2->next;
            } else {
                tail->next = list1;
                //list1, tail = list1->next, list1;
                list1 = list1->next;
            }
            tail = tail->next;
        }

        // Append the remaining elements from list1 or list2
        // cpp처럼 if (list1 || list2)으로 밖을 감싸주면 Runtime error : member access within misaligned address 
        if (list1) {tail->next = list1;} 
        else {tail->next = list2;}

        return dummy->next;
    }
