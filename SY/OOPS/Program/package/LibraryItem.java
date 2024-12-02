package library;

public abstract class LibraryItem {
    protected String author;
    protected String title;
    protected String date;

    public LibraryItem(String author, String title, String date) {
        this.author = author;
        this.title = title;
        this.date = date;
    }

    // Getter methods
    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public String getDate() {
        return date;
    }

    @Override
    public String toString() {
        return "Title: " + title + ", Author: " + author + ", Date: " + date;
    }
}
