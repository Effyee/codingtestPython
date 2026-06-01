import java.util.*;

class Solution {

    class Song {
        int idx;
        int play;

        Song(int idx, int play) {
            this.idx = idx;
            this.play = play;
        }
    }

    public int[] solution(String[] genres, int[] plays) {

        HashMap<String, Integer> genrePlay = new HashMap<>();
        HashMap<String, ArrayList<Song>> genreSongs = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {

            genrePlay.put(
                genres[i],
                genrePlay.getOrDefault(genres[i], 0) + plays[i]
            );

            genreSongs.putIfAbsent(
                genres[i],
                new ArrayList<>()
            );

            genreSongs.get(genres[i])
                      .add(new Song(i, plays[i]));
        }

        ArrayList<String> genreList =
            new ArrayList<>(genrePlay.keySet());

        genreList.sort(
            (a, b) -> genrePlay.get(b) - genrePlay.get(a)
        );

        ArrayList<Integer> result =
            new ArrayList<>();

        for (String genre : genreList) {

            ArrayList<Song> songs =
                genreSongs.get(genre);

            songs.sort((a, b) -> {
                if (a.play == b.play)
                    return a.idx - b.idx;

                return b.play - a.play;
            });

            for (int i = 0;
                 i < Math.min(2, songs.size());
                 i++) {

                result.add(songs.get(i).idx);
            }
        }

        return result.stream()
                     .mapToInt(i -> i)
                     .toArray();
    }
}