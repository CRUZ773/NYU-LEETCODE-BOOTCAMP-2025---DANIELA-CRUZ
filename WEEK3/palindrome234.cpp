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


 // C++ SOLUTION
class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        ListNode *curr = head;
        ListNode *next;
        stack<int> pal_stack;
        while (curr != nullptr)
        {
            pal_stack.push(curr->val);
            curr = curr->next;
        }

        curr = head;

        while (curr != nullptr)
        {
            int top_stack = pal_stack.top();
            pal_stack.pop();
            if (curr->val != top_stack)
            {
                return false;
            }
            else
            {
                curr = curr->next;
            }
        }
        return true;
    }
};