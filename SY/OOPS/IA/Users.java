public abstract class Users {
  private String id;
  private String name;
  private int age;

  public Users(String id, String name, int age) {
      this.id = id;
      this.name = name;
      this.age = age;
  }

  public String getId() { return id; }
  public String getName() { return name; }
  public void setName(String name) { this.name = name; }
  public int getAge() { return age; }

  public abstract String getRole();
}
