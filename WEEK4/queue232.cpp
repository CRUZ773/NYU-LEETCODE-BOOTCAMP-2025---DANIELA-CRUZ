class MyQueue
{
private:
    stack<int> first_in;  // incoming elements
    stack<int> first_out; // outgoing elements
public:
    MyQueue()
    {
    }

    void push(int x)
    {
        first_in.push(x);
    }

    int pop()
    {
        if (first_out.empty())
        {
            // Move elements
            while (!first_in.empty())
            {
                first_out.push(first_in.top());
                first_in.pop();
            }
        }
        int val = first_out.top();
        first_out.pop();
        return val;
    }

    int peek()
    {
        if (first_out.empty())
        {
            // Move elements
            while (!first_in.empty())
            {
                first_out.push(first_in.top());
                first_in.pop();
            }
        }
        return first_out.top();
    }

    bool empty()
    {
        return first_in.empty() && first_out.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */