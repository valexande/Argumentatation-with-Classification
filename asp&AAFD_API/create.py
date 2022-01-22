

class arg():

    def __init__(self):
        pass


    def createFile(self, argument, att):

        f = open('framework.lp', 'a')
        #write the arguments
        helper = ""
        for i in range(int(argument)):
            helper = helper + "a" + str(i) + ";"
        helper = helper + "|"
        helper = helper.replace(";|", "")
        f.write('argument(' + str(helper) + ').\n')

        #write the attacks
        att = att.split(',')
        for a in att:
            a = a.split('-')
            if a[2] == "cf":
                a[2] = "conflict"
            elif a[2] == "def":
                a[2] = "defending"
            elif a[2] == "no":
                a[2] = "normal"
            else:
                pass
            f.write('attacks(' + str(a[0]) + ', ' + str(a[1]) + ', ' + str(a[2]) +').\n')

        f.write('\n\n')

        f.close()

        return 1