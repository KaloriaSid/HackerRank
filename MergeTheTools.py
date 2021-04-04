def merge_the_tools(string, k):
    import textwrap
    wrapper = wrapper = textwrap.TextWrapper(width=k)
    result = wrapper.fill(text=string)
    l = result.split()
    for word in l:
        u = []
        for i in word:
            if i not in u:
                print(i, end='')
                u.append(i)
        print()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
