import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {

        char[][] map = new char[park.length][park[0].length()];

        for(int i = 0; i < park.length; i++){
            map[i] = park[i].toCharArray();
        }

        int x = 0;
        int y = 0;

        for(int i = 0; i < park.length; i++){
            for(int j = 0; j < park[0].length(); j++){
                if(map[i][j] == 'S'){
                    x = i;
                    y = j;
                }
            }
        }

        for(String route : routes){

            String[] parts = route.split(" ");

            char dir = parts[0].charAt(0);
            int count = Integer.parseInt(parts[1]);

            int dx = 0;
            int dy = 0;

            if(dir == 'E'){
                dx = 0;
                dy = 1;
            }
            else if(dir == 'W'){
                dx = 0;
                dy = -1;
            }
            else if(dir == 'S'){
                dx = 1;
                dy = 0;
            }
            else if(dir == 'N'){
                dx = -1;
                dy = 0;
            }

            int nx = x;
            int ny = y;

            boolean flag = true;

            for(int i = 0; i < count; i++){

                nx += dx;
                ny += dy;

                if(nx < 0 || nx >= park.length ||
                   ny < 0 || ny >= park[0].length()){
                    flag = false;
                    break;
                }

                if(map[nx][ny] == 'X'){
                    flag = false;
                    break;
                }
            }

            if(flag){
                x = nx;
                y = ny;
            }
        }

        return new int[]{x, y};
    }
}