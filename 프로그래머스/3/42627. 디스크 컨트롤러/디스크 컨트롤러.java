import java.util.*;

class Solution {

    class Job {
        int request;
        int duration;

        Job(int request, int duration) {
            this.request = request;
            this.duration = duration;
        }
    }

    public int solution(int[][] jobs) {

        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);

        PriorityQueue<Job> pq =
                new PriorityQueue<>((a, b) -> a.duration - b.duration);

        int time = 0;
        int idx = 0;
        int total = 0;
        int count = 0;

        while (count < jobs.length) {

            while (idx < jobs.length && jobs[idx][0] <= time) {
                pq.offer(new Job(jobs[idx][0], jobs[idx][1]));
                idx++;
            }

            if (pq.isEmpty()) {
                time = jobs[idx][0];
                continue;
            }

            Job cur = pq.poll();

            time += cur.duration;

            total += (time - cur.request);

            count++;
        }

        return total / jobs.length;
    }
}