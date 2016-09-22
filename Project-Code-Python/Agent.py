# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
#import numpy

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    def Solve(self,problem):

        print problem.problemType
        print "Verbal: %s" % problem.hasVerbal
        print "Visual: %s" % problem.hasVisual

        # Records the relationships
        semantic = {}
        # Creates a list of all the figures given
        shapes = {}
        # List of all solutions figures given
        solutions = {}
        # List of key and array of object keys
        solutionsKeyValue = {}
        # List of all Attributes to be defined
        allAttributes = [];



        for figureName in problem.figures:
            # currFigure = problem.figures[figureName].objects
            currFigure = problem.figures[figureName]
            check = str(figureName)
            if check.isalpha():
                shapes[check] = currFigure
                for x,y in currFigure.objects.iteritems():
                    print x
                print"Look above"
            else:
                solutions[check] = currFigure
                for key,value in currFigure.objects.iteritems():
                    solutionsKeyValue[check] = key


        print solutionsKeyValue
        attributesFigure1 = shapes["A"].objects["a"].attributes
        attributesFigure2 = shapes["B"].objects["b"].attributes
        attributesFigure3 = {}

        if attributesFigure1 is not None and attributesFigure2 is not None:
            for x,y in attributesFigure1.iteritems():
                allAttributes.append(x)

        for attribute in allAttributes:
            if attributesFigure1[attribute] == attributesFigure2[attribute]:
                attributes = {}
                attributes['change'] = False
                attributes['from'] = attributesFigure1[attribute]
                attributes['to'] = attributesFigure2[attribute]
                semantic[attribute] = attributes
            else:
                attributes = {}
                attributes['change'] = True
                attributes['from'] = attributesFigure1[attribute]
                attributes['to'] = attributesFigure2[attribute]
                semantic[attribute] = attributes

        attributesFigure3 = shapes['C'].objects['c'].attributes
        attributesFigure4 = {}

        for cursor in allAttributes:
            if semantic[cursor]["change"]:
                print "Do something on line 88"
            else:
                attributesFigure4[cursor] = attributesFigure3[cursor]

        #Time to test against given options


        finalSolution = self.compare(attributesFigure4,solutions,solutionsKeyValue,allAttributes)



        print "Done"




        return int(finalSolution)

    def compare(self,answer,solutions,solutionsKeys,attributes):
        for key, value in solutionsKeys.iteritems():
            currSolution = solutions[key].objects[value].attributes
            counter = 0
            for attribute in attributes:
                if answer[attribute] == currSolution[attribute]:
                    counter = counter + 1
                else:
                    print ""
            if counter == len(attributes):
                print "Found it %s" % key
                return key
