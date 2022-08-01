from subprocess import STDOUT, PIPE, Popen
import os

class compute():

    def __init__(self, problem, choiceExtension):
        self.problem = problem
        self.choiceExtension = choiceExtension

    def cleaner(self, pfinal):##function to clean the answers for gr, pr, st. We use asprin for these thus we get a not so clean result
        pfinal = pfinal.split('Answer: ')

        del pfinal[0]

        helperFinal = []
        helperGeneral = []
        for line in pfinal:
            if "\nOPTIMUM FOUND\n" in line:
                helperFinal.append(line.split("\nOPTIMUM FOUND\n")[0].replace("\n", ""))

        for line in pfinal:
            if "Models       :" in line:
                helper = str(line.split("Models       :")[1])
                print(helper)
                helperNew = helper.split("(asprin) (venv)")[0]
                helperGeneral.append("Models       :" + str(helperNew))

        final = []
        if self.choiceExtension == "gr":
            for line in helperFinal:
                line = line[1:]
                line = line.replace("co_", " gr_")
                final.append('Answer: ' + line + '\n')
        elif self.choiceExtension == "pr":
            for line in helperFinal:
                line = line[1:]
                line = line.replace("ad_", " pr_")
                final.append('Answer: ' + line + '\n')
        elif self.choiceExtension == "st":
            for line in helperFinal:
                line = line[1:]
                line = line.replace("cf_", " st_")
                final.append('Answer: ' + line + '\n')
        else:
            pass


        finalString = ""
        for f in final:
            finalString = finalString + f

        print(finalString)
        #finalString = finalString + helperGeneral[0].replace("\n\n", "\n")


        return finalString

    def pasteExtension(self):

        f = open("semantics.lp", "a")
        if self.choiceExtension == "cf":
            text = """% Conflict free Extension (Def 3)\n
                      % Generate all possible extensions\n
                      {cf_extension(A) : argument(A)}.\n
                      :- cf_extension(A1), cf_extension(A2), attacks(A1, A2, conflict).\n
                      #show cf_extension/1."""
            f.write(text)
        elif self.choiceExtension == "a":
            text = """% Conflict free Extension (Def 3)\n
                      % Generate all possible extensions\n
                      {cf_extension(A) : argument(A)}.\n
                      :- cf_extension(A1), cf_extension(A2), attacks(A1, A2, conflict).\n\n 
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Admissible Extension (Def 4)\n\n
                      ad_extension(A) :- cf_extension(A).\n\n
                      % There is a conflict attack on argument A\n
                      argumentGetsConfAttack(A) :- argument(A),attacks(_, A, conflict).    % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by all extensions\n
                      defendedByExtension(A) :- argument(A),not argumentGetsConfAttack(A). % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by the current extension\n
                      defendedByExtension(A) :- argument(A),  attacks(A1, A, conflict),attacks(A2, A1, defending),attacks(A2, A1, defending),attacks(A2, A1, defending),ad_extension(A2).\n
                      % Notice! It should not be ad_extension(A) here\n\n
                      :- ad_extension(A), not defendedByExtension(A).\n
                      #show ad_extension/1."""
            f.write(text)
        elif self.choiceExtension == "co":
            text = """% Conflict free Extension (Def 3)\n
                      % Generate all possible extensions\n
                      {cf_extension(A) : argument(A)}.\n
                      :- cf_extension(A1), cf_extension(A2), attacks(A1, A2, conflict).\n\n 
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Admissible Extension (Def 4)\n\n
                      ad_extension(A) :- cf_extension(A).\n\n
                      % There is a conflict attack on argument A\n
                      argumentGetsConfAttack(A) :- argument(A),attacks(_, A, conflict).    % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by all extensions\n
                      defendedByExtension(A) :- argument(A),not argumentGetsConfAttack(A). % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by the current extension\n
                      defendedByExtension(A) :- argument(A),  attacks(A1, A, conflict),attacks(A2, A1, defending),attacks(A2, A1, defending),attacks(A2, A1, defending),ad_extension(A2).\n
                      % Notice! It should not be ad_extension(A) here\n\n
                      :- ad_extension(A), not defendedByExtension(A).\n\n
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Complete Extension (Def 5)\n\n
                      co_extension(A) :- ad_extension(A).\n\n
                      % Some argument A attacks the current extension\n
                      attacksExtension(A) :- attacks(A, A1, conflict), co_extension(A1).\n\n
                      % Some argument A attacks the current extension\n
                      getsAttackedByExtension(A) :- attacks(A1, A, conflict), co_extension(A1).\n
                      compliantArg(A) :-defendedByExtension(A), not getsAttackedByExtension(A), not attacksExtension(A).\n
                      :- compliantArg(A), not co_extension(A).\n
                      #show co_extension/1."""
            f.write(text)
        elif self.choiceExtension == "gr":
            text = """% Conflict free Extension (Def 3)\n
                      % Generate all possible extensions\n
                      {cf_extension(A) : argument(A)}.\n
                      :- cf_extension(A1), cf_extension(A2), attacks(A1, A2, conflict).\n\n 
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Admissible Extension (Def 4)\n\n
                      ad_extension(A) :- cf_extension(A).\n\n
                      % There is a conflict attack on argument A\n
                      argumentGetsConfAttack(A) :- argument(A),attacks(_, A, conflict).    % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by all extensions\n
                      defendedByExtension(A) :- argument(A),not argumentGetsConfAttack(A). % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by the current extension\n
                      defendedByExtension(A) :- argument(A),  attacks(A1, A, conflict),attacks(A2, A1, defending),attacks(A2, A1, defending),attacks(A2, A1, defending),ad_extension(A2).\n
                      % Notice! It should not be ad_extension(A) here\n\n
                      :- ad_extension(A), not defendedByExtension(A).\n\n
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Complete Extension (Def 5)\n\n
                      co_extension(A) :- ad_extension(A).\n\n
                      % Some argument A attacks the current extension\n
                      attacksExtension(A) :- attacks(A, A1, conflict), co_extension(A1).\n\n
                      % Some argument A attacks the current extension\n
                      getsAttackedByExtension(A) :- attacks(A1, A, conflict), co_extension(A1).\n
                      compliantArg(A) :-defendedByExtension(A), not getsAttackedByExtension(A), not attacksExtension(A).\n
                      :- compliantArg(A), not co_extension(A).\n\n
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Grounded Extension (Def 6)\n
                      #preference(p1,subset){co_extension(A)}.\n
                      #optimize(p1).\n
                      #show co_extension/1.
                     """
            f.write(text)
        elif self.choiceExtension == "pr":
            text = """% Conflict free Extension (Def 3)\n
                      % Generate all possible extensions\n
                      {cf_extension(A) : argument(A)}.\n
                      :- cf_extension(A1), cf_extension(A2), attacks(A1, A2, conflict).\n\n 
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Admissible Extension (Def 4)\n\n
                      ad_extension(A) :- cf_extension(A).\n\n
                      % There is a conflict attack on argument A\n
                      argumentGetsConfAttack(A) :- argument(A),attacks(_, A, conflict).    % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by all extensions\n
                      defendedByExtension(A) :- argument(A),not argumentGetsConfAttack(A). % Notice! It should not be ad_extension(A) here\n\n
                      % Argument A is defended by the current extension\n
                      defendedByExtension(A) :- argument(A),  attacks(A1, A, conflict),attacks(A2, A1, defending),attacks(A2, A1, defending),attacks(A2, A1, defending),ad_extension(A2).\n
                      % Notice! It should not be ad_extension(A) here\n\n
                      :- ad_extension(A), not defendedByExtension(A).\n\n
                      %%%%%%%%%%%%%%%%%%%%%\n
                      % Preferred Extension (Def 7)\n\n
                      #preference(p1,superset){ad_extension(A)}.\n
                      #optimize(p1).\n
                      #show ad_extension/1.
                      """
            f.write(text)
        elif self.choiceExtension == "st":

            text = """
            %%%%%%%%%%%%%%%%%%%%%\n
            % Conflict free Extension (Def 3)\n\n
            % Generate all possible extensions\n
            {cf_extension(A) : argument(A)}.\n\n
            :- cf_extension(A1), cf_extension(A2), attacks(A1, A2, conflict).\n\n\n\n
            %%%%%%%%%%%%%%%%%%%%%\n
            % Stable Extension (Def 8)\n\n
            #preference(p1,superset){cf_extension(A)}.\n
            #optimize(p1).\n\n
            other(A) :- argument(A), not cf_extension(A), cf_extension(B), attacks(B,A, defending).
            :- argument(A), not other(A), not cf_extension(A). 
            
            %other(A) :- argument(A), not cf_extension(A).\n
            %validAttack(A) :- other(A), cf_extension(B), attacks(B, A, defending).\n
            %:- #count{A: other(A)} = X, #count{B: validAttack(B)} = Y, X != Y.\n         
            #show cf_extension/1.\n
            """
            f.write(text)
        else:
            pass

        f.close()

        return 1

    def Remove(self, list_results):
        final_list = []
        for num in list_results:
            if num not in final_list:
                final_list.append(num)
        return final_list

    def query(self):

        pfinal = ""
        if self.problem == "1":
            if self.choiceExtension in ['cf', 'a', 'co']:
                os.chdir('C:/Users/Alex Vassiliades/PycharmProjects/classificationAPI/asp&AAFD_API')
                p = Popen(str('clingo semantics.lp framework.lp 0'), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                grep_stdout = p.communicate()
                pfinal = str(grep_stdout[0].decode('utf-8'))
                return pfinal
            else:
                os.chdir('C:/Users/Alex Vassiliades/PycharmProjects/classificationAPI/asp&AAFD_API')
                cmds = ["conda activate asprin", "asprin semantics.lp framework.lp 0", "conda deactivate"]
                p = Popen('cmd.exe', stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding='ISO-8859-1')
                for cmd in cmds:
                    p.stdin.write(cmd + "\n")
                p.stdin.close()
                pfinal = p.stdout.read()
                pfinal = self.cleaner(pfinal)  ##here also notice
                return pfinal
        elif self.problem == "2":
            if self.choiceExtension in ['cf', 'a', 'co']:
                os.chdir('C:/Users/Alex Vassiliades/PycharmProjects/classificationAPI/asp&AAFD_API')
                p = Popen(str('clingo semantics.lp framework.lp 1'), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
                grep_stdout = p.communicate()
                pfinal = str(grep_stdout[0].decode('utf-8'))
                return pfinal
            else:
                os.chdir('C:/Users/Alex Vassiliades/PycharmProjects/classificationAPI/asp&AAFD_API')
                cmds = ["conda activate asprin", "asprin semantics.lp framework.lp 1", "conda deactivate"]
                p = Popen('cmd.exe', stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding='ISO-8859-1')
                for cmd in cmds:
                    p.stdin.write(cmd + "\n")
                p.stdin.close()
                pfinal = p.stdout.read()
                pfinal = self.cleaner(pfinal)  ##here also notice
                return pfinal

        return pfinal