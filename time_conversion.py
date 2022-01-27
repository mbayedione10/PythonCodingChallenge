def timeConversion(s):
    # Write your code here
    if s.endswith('AM'):
        if s[:2] == "12":
            s = s.replace(s[:2], "00")
            return s[:-2]
        return s[:-2]
    if s.endswith('PM'):
        hour = int(s[:2]) + 12
        if hour < 24:
            s = s.replace(s[:2], str(hour))
        return s[:-2]


if __name__ == '__main__':
    s = input("Input Format : hh:mm:ssAM or hh:mm:ss:PM: ")
    result = timeConversion(s)

    print(result)
