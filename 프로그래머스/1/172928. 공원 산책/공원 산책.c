#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int* solution(const char* park[], size_t park_len, const char* routes[], size_t routes_len) {

    int* answer = (int*)malloc(sizeof(int)*2);
    
    int x=0, y=0;
    int row=park_len;
    int col=strlen(park[0]);
    
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            if(park[i][j]=='S'){
                x=i;
                y=j;
            }
        }
    }
    
    for(int i=0;i<routes_len;i++){
        
        char direction;
        int distance;
        
        sscanf(routes[i],"%c %d", &direction, &distance);
        
        int dx=0, dy=0;
        int nx=x, ny=y;
        
        if(direction=='N'){
            dx=-1;
            dy=0;
        }
        else if(direction=='S'){
            dx=1;
            dy=0;
        }
        else if(direction=='W'){
            dx=0;
            dy=-1;
        }
        else{
            dx=0;
            dy=1;
        }
        for(int i=0;i<distance;i++){
            if(nx+dx>=0 && ny+dy>=0 && nx+dx<row && ny+dy<col&& park[nx+dx][ny+dy]!='X'){
                nx+=dx;
                ny+=dy;
            }else{
                nx=x;
                ny=y;
                break;
            }
        }
        x=nx;
        y=ny;
    }
    answer[0]=x;
    answer[1]=y;
    return answer;
}