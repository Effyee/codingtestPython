#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct _node {
    int idx;
    struct _node* nx[26];
} node;
node* create_node() {
    node* np = (node*)malloc(sizeof(node));
    for(int i = 0; i < 26; i++) np->nx[i] = NULL;
    return np;
}
void delete_node(node* np) {
    for(int i = 0; i < 26; i++) {
        if(np->nx[i]) delete_node(np->nx[i]);
    }
    free(np);
}
void add_node(node* root, char* str, int idx) {
    node* np = root;
    while(*str) {
        int i = *str++ - 'a';
        if(!np->nx[i]) np->nx[i] = create_node();
        np = np->nx[i];
    }
    np->idx = idx;
}
int find_idx(node* root, char* str) {
    node* np = root;
    while(*str) {
        int i = *str++ - 'a';
        np = np->nx[i];
    }
    return np->idx;
}
void swap(char** a, char** b) {
    char* tmp = *a;
    *a = *b;
    *b = tmp;
}
char** solution(const char* players[], size_t players_len, const char* callings[], size_t callings_len) {
    char** answer = (char**)malloc(players_len * sizeof(char*));
    node* root = create_node();
    for(int i = 0; i < players_len; i++) {
        answer[i] = (char*)malloc((strlen(players[i]) + 1) * sizeof(char));
        strcpy(answer[i], players[i]);
        add_node(root, players[i], i);
    }
    for(int i = 0; i < callings_len; i++) {
        int idx = find_idx(root, callings[i]);
        add_node(root, answer[idx], idx - 1);
        add_node(root, answer[idx - 1], idx);
        swap(&answer[idx], &answer[idx - 1]);
    }

    delete_node(root);
    return answer;
}