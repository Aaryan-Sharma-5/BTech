#include <bits/stdc++.h>
using namespace std;

string ipclass(string ip)
{
  int first = stoi(ip.substr(0, ip.find('.')));
  if (first >= 1 && first <= 126)
    return "A (1.0.0.0 - 126.255.255.255)";
  else if (first >= 128 && first <= 191)
    return "B (128.0.0.0 - 191.255.255.255)";
  else if (first >= 192 && first <= 223)
    return "C (192.0.0.0 - 223.255.255.255)";
  else if (first >= 224 && first <= 239)
    return "D (Multicast) (224.0.0.0 - 239.255.255.255)";
  else if (first >= 240 && first <= 254)
    return "E (Experimental) (240.0.0.0 - 254.255.255.255)";
  else
    return "Invalid IP";
}

bool is_classful(string ip)
{
  return ip.find('/') == string::npos;
}

string get_subnet_mask(string ip_class)
{
  if (ip_class.find("A") != string::npos)
    return "255.0.0.0";
  else if (ip_class.find("B") != string::npos)
    return "255.255.0.0";
  else if (ip_class.find("C") != string::npos)
    return "255.255.255.0";
  else if (ip_class.find("D") != string::npos || ip_class.find("E") != string::npos)
    return "N/A (Multicast/Experimental address)";
  else
    return "Invalid IP class";
}

string cidr_to_subnet_mask(int prefix_length)
{
  uint32_t mask = 0xFFFFFFFF;
  mask = mask << (32 - prefix_length);

  vector<int> octets(4);
  for (int i = 3; i >= 0; i--)
  {
    octets[i] = mask & 0xFF;
    mask >>= 8;
  }

  stringstream ss;
  ss << octets[0] << "." << octets[1] << "." << octets[2] << "." << octets[3];
  return ss.str();
}

int main()
{
  string ip_input;
  cout << "Enter an IP address: ";
  cin >> ip_input;

  string ip_part = ip_input.substr(0, ip_input.find('/'));
  string ip_class = ipclass(ip_part);

  cout << "IP Address Class: " << ip_class << endl;

  if (is_classful(ip_input))
  {
    cout << "Addressing Type: Classful" << endl;
    string subnet_mask = get_subnet_mask(ip_class);
    cout << "Subnet Mask: " << subnet_mask << endl;
  }
  else
  {
    cout << "Addressing Type: Classless" << endl;

    size_t slash_pos = ip_input.find('/');
    int prefix_length = stoi(ip_input.substr(slash_pos + 1));

    if (prefix_length < 0 || prefix_length > 32)
    {
      cout << "Invalid prefix length!" << endl;
    }
    else
    {
      string subnet_mask = cidr_to_subnet_mask(prefix_length);
      cout << "Subnet Mask: " << subnet_mask << endl;
    }
  }

  return 0;
}
