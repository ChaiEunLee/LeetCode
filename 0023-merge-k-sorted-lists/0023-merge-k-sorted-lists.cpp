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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode * dummy = new ListNode(0); // cpp에서는 new를 붙여서 새로운 노드를 만들어야함
        ListNode * tail = dummy;

        // Until one of two list reached end
        while (list1 and list2){
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
        // One element from one of two list will be remained
        if (list1 or list2){
            if (list1){tail->next = list1;}
            else {tail->next = list2;}
        }
        return dummy->next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()){return nullptr;}

        vector<ListNode*> list_;
        list_.push_back(lists[0]);
        for (int i=1; i<lists.size(); ++i){
            ListNode * x = mergeTwoLists(list_[i-1], lists[i]);
            list_.push_back(x);
        }
        return list_.back();
    }
};
