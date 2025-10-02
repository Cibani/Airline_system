public class Main {
    public static void main(String[] args) {
        SongDAO dao = new SongDAO();

        // Add sample song
        Song s1 = new Song("Shape of You", "Ed Sheeran", "Divide", "Pop", 2017);
        dao.addSong(s1);

        // Fetch songs
        for (Song s : dao.getAllSongs()) {
            System.out.println(s.getTitle() + " - " + s.getArtist());
        }
    }
}
