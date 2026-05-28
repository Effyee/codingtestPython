#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int bandage[], size_t bandage_len,
             int health,
             int** attacks,
             size_t attacks_rows,
             size_t attacks_cols) {

    int t = bandage[0];
    int x = bandage[1];
    int y = bandage[2];

    int max_health = health;

    int attacks_idx = 0;
    int cont = 0;

    int last_time = attacks[attacks_rows - 1][0];

    for(int i = 1; i <= last_time; i++) {

        // 공격
        if(i == attacks[attacks_idx][0]) {

            health -= attacks[attacks_idx][1];

            if(health <= 0) {
                return -1;
            }

            cont = 0;
            attacks_idx++;
        }

        // 회복
        else {

            health += x;
            cont++;

            if(cont == t) {
                health += y;
                cont = 0;
            }

            if(health > max_health) {
                health = max_health;
            }
        }
    }

    return health;
}