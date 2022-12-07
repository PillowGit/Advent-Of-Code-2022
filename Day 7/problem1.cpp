#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <stack>


class TreeNode {
public:
    std::vector<TreeNode*> children;
    TreeNode* parent;
    std::vector<int> files;
    unsigned long int size;
    std::string name;


    TreeNode(TreeNode* par, const std::string& name_) : parent(par), name(name_), size(0) {}

    TreeNode* GetChild(const std::string& name) {
        for (TreeNode* t : children)
            if (t->name == name) return t;
    }

    void AddFile(int x) { files.push_back(x); }

    unsigned long int CalculateSize() {
        unsigned long int total = 0;
        for (int x : files) total += x;
        for (TreeNode* t : children) total += t->size;
        size = total;
        return size;
    }

};

int main() {

    std::ifstream input_file;
    input_file.open("input.txt");
    std::string line;
    TreeNode* root = new TreeNode(nullptr, "/");
    TreeNode* curr = root;

    // Tree construction
    while (!input_file.eof()) {
        std::getline(input_file, line);

        if (line[0] != '$') { // if not reading command

            if (line.substr(0, 3) == "dir") { // if looking at new folder
                curr->children.push_back(new TreeNode(curr, line.substr(4))); // add new folder
                std::cout << "Making new folder called " + line.substr(4) + "\n";
            }
            else {
                curr->files.push_back(std::stoi(line.substr(0, line.find(' ')))); // add file sizes
                std::cout << "Adding a new file of size " << std::stoi(line.substr(0, line.find(' '))) << std::endl;
            }
        }
        else { // now if reading a command
            if (line.substr(2, 2) == "ls") { // if listing items
                std::cout << "listing files...\n";
            }
            else { // if cd into
                std::string cd_into = line.substr(5);
                std::cout << "cd into " + cd_into + "\n";
                if (cd_into == "..") curr = curr->parent;
                else if (cd_into == "/") curr = root;
                else curr = curr->GetChild(cd_into);
            }
        }
    }

    // Now backwards bfs for file sizes!
    std::stack<TreeNode*> s;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        root = q.front();
        q.pop();
        s.push(root);
        for (TreeNode* t : root->children) q.push(t);
    }
    unsigned long int target_size = 100000;
    unsigned long long int total = 0;
    while (!s.empty()) {
        root = s.top();
        if (root->CalculateSize() < target_size) total += root->size;
        s.pop();
    }

    std::cout << "And finally, the amount is: " << total << std::endl;

    input_file.close();
    return 0;
}