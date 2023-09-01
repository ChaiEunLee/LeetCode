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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode * second = list1;
        ListNode * first = second;
        int i = 0, j = 0;

        // For reaching ath node
        while (i != a-1){
            first = first->next;
            i++;
        }

        // For reaching bth node
        while (j != b){
            second = second->next;
            j++;
        }

        // Connecting the first runner with second list
        first->next = list2;

        // Until we reach the end of list2 we are connecting first and list2
        while (list2->next){
            list2 = list2->next;
        }

        // Connecting the remaining part of list1
        list2->next = second->next;

        return list1;
    }
};