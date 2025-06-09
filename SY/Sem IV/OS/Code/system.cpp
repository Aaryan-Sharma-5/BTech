#include <bits/stdc++.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <unistd.h>
#include <cstring>
#define endl '\n'
using namespace std;

int main()
{
    pid_t pid = fork();

    if (pid < 0)
    {
        cerr << "Fork failed" << endl;
        return 1;
    }
    else if (pid == 0)
    {
        // Child process
        cout << "Child Process:" << endl;
        cout << "PID: " << getpid() << endl;
        
        sleep(1); // Ensure parent doesn’t terminate before printing PPID
        cout << "PPID: " << getppid() << endl;
        cout << "Fork return value: " << pid << endl;

        // Open the file
        int fd = open("aa.txt", O_RDONLY);
        if (fd < 0)
        {
            cerr << "Failed to open file: " << strerror(errno) << endl;
            return 1;
        }

        // Read the file contents
        char buffer[1025]; // Increased buffer size
        ssize_t bytesRead;
        while ((bytesRead = read(fd, buffer, sizeof(buffer) - 1)) > 0)
        {
            buffer[bytesRead] = '\0'; // Null-terminate the buffer safely
            cout << buffer;
        }

        // Close the file
        close(fd);
    }
    else
    {
        // Parent process
        cout << "Parent Process:" << endl;
        cout << "PID: " << getpid() << endl;
        cout << "PPID: " << getppid() << endl;
        cout << "Fork return value: " << pid << endl;

        // Wait for the child process to complete
        wait(NULL);
    }

    return 0;
}
