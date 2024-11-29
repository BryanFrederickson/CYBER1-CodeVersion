from pathlib import Path # for parsing filepath
import ast as ast # for testing validity of Python file
import libcst as cst # LibCST library for editing source code
import random # used for randomly choosing placeholder names
import re # for regular expressions
from libcst.metadata import MetadataWrapper, ParentNodeProvider # for in-depth cst node parsing
import google.generativeai as genai # for generating synonyms


'''
Parse and Test Input File

'''
print("Input the filepath for input Python file. In Windows file explorer, select the file then shift right click, then select \'Copy as path\'. Paste into terminal using right click.")
while True:
    input_path=input("Filepath: ")
    path=Path(input_path.replace('"', ''))
    if not path.exists():
        print(f"Could not find {input_path}!")
    elif not path.is_file():
        print("Not a file!")
    elif not path.suffix == '.py':
        print("Not a python file!")
    else:
        try:
            with open(path, 'r') as input_file:
                print(f"{path.name} opened successfully.")
                source_code=input_file.read()
                try:
                    ast.parse(source_code)
                    print(f"{path.name} is syntactically valid.")
                    break
                except SyntaxError as error:
                    print(f"Syntax error in {path.name}: {error}")
        except FileNotFoundError:
            print(f"Could not find {input_path}!")
        except IOError:
            print(f"{path.name} could not be opened!")

original_cst=cst.parse_module(source_code)

'''
Rename Variables

'''

# animal wordbank list from: https://gist.github.com/CheeseCake87/c1d222c387ff1342cf3b910456f4865a
animals = ['Canidae', 'Felidae', 'Cat', 'Cattle', 'Dog', 'Donkey', 'Goat', 'Horse', 'Pig', 'Rabbit',
           'Aardvark', 'Aardwolf', 'Albatross', 'Alligator', 'Alpaca', 'Amphibian', 'Anaconda',
           'Angelfish', 'Anglerfish', 'Ant', 'Anteater', 'Antelope', 'Antlion', 'Ape', 'Aphid',
           'Armadillo', 'Asp', 'Baboon', 'Badger', 'Bandicoot', 'Barnacle', 'Barracuda', 'Basilisk',
           'Bass', 'Bat', 'Bear', 'Beaver', 'Bedbug', 'Bee', 'Beetle', 'Bird', 'Bison', 'Blackbird',
           'Boa', 'Boar', 'Bobcat', 'Bobolink', 'Bonobo', 'Bovid', 'Bug', 'Butterfly', 'Buzzard',
           'Camel', 'Canid', 'Capybara', 'Cardinal', 'Caribou', 'Carp', 'Cat', 'Catshark',
           'Caterpillar', 'Catfish', 'Cattle', 'Centipede', 'Cephalopod', 'Chameleon', 'Cheetah',
           'Chickadee', 'Chicken', 'Chimpanzee', 'Chinchilla', 'Chipmunk', 'Clam', 'Clownfish',
           'Cobra', 'Cockroach', 'Cod', 'Condor', 'Constrictor', 'Coral', 'Cougar', 'Cow', 'Coyote',
           'Crab', 'Crane', 'Crawdad', 'Crayfish', 'Cricket', 'Crocodile', 'Crow', 'Cuckoo', 'Cicada',
           'Damselfly', 'Deer', 'Dingo', 'Dinosaur', 'Dog', 'Dolphin', 'Donkey', 'Dormouse', 'Dove',
           'Dragonfly', 'Dragon', 'Duck', 'Eagle', 'Earthworm', 'Earwig', 'Echidna', 'Eel', 'Egret',
           'Elephant', 'Elk', 'Emu', 'Ermine', 'Falcon', 'Ferret', 'Finch', 'Firefly', 'Fish',
           'Flamingo', 'Flea', 'Fly', 'Flyingfish', 'Fowl', 'Fox', 'Frog', 'Gamefowl', 'Galliform',
           'Gazelle', 'Gecko', 'Gerbil', 'Gibbon', 'Giraffe', 'Goat', 'Goldfish', 'Goose', 'Gopher',
           'Gorilla', 'Grasshopper', 'Grouse', 'Guan', 'Guanaco', 'Guineafowl', 'Gull', 'Guppy',
           'Haddock', 'Halibut', 'Hamster', 'Hare', 'Harrier', 'Hawk', 'Hedgehog', 'Heron', 'Herring',
           'Hippopotamus', 'Hookworm', 'Hornet', 'Horse', 'Hoverfly', 'Hummingbird', 'Hyena', 'Iguana',
           'Impala', 'Jackal', 'Jaguar', 'Jay', 'Jellyfish', 'Junglefowl', 'Kangaroo', 'Kingfisher',
           'Kite', 'Kiwi', 'Koala', 'Koi', 'Krill', 'Ladybug', 'Lamprey', 'Landfowl', 'Lark', 'Leech',
           'Lemming', 'Lemur', 'Leopard', 'Leopon', 'Limpet', 'Lion', 'Lizard', 'Llama', 'Lobster',
           'Locust', 'Loon', 'Louse', 'Lungfish', 'Lynx', 'Macaw', 'Mackerel', 'Magpie', 'Mammal',
           'Manatee', 'Mandrill', 'Marlin', 'Marmoset', 'Marmot', 'Marsupial', 'Marten', 'Mastodon',
           'Meadowlark', 'Meerkat', 'Mink', 'Minnow', 'Mite', 'Mockingbird', 'Mole', 'Mollusk',
           'Mongoose', 'Monkey', 'Moose', 'Mosquito', 'Moth', 'Mouse', 'Mule', 'Muskox', 'Narwhal',
           'Newt', 'Nightingale', 'Ocelot', 'Octopus', 'Opossum', 'Orangutan', 'Orca', 'Ostrich',
           'Otter', 'Owl', 'Ox', 'Panda', 'Panther', 'Parakeet', 'Parrot', 'Parrotfish', 'Partridge',
           'Peacock', 'Peafowl', 'Pelican', 'Penguin', 'Perch', 'Pheasant', 'Pig', 'Pigeon', 'Pike',
           'Pinniped', 'Piranha', 'Planarian', 'Platypus', 'Pony', 'Porcupine', 'Porpoise', 'Possum',
           'Prawn', 'Primate', 'Ptarmigan', 'Puffin', 'Puma', 'Python', 'Quail', 'Quelea', 'Quokka',
           'Rabbit', 'Raccoon', 'Rat', 'Rattlesnake', 'Raven', 'Reindeer', 'Reptile', 'Rhinoceros',
           'Roadrunner', 'Rodent', 'Rook', 'Rooster', 'Roundworm', 'Sailfish', 'Salamander', 'Salmon',
           'Sawfish', 'Scallop', 'Scorpion', 'Seahorse', 'Shark', 'Sheep', 'Shrew', 'Shrimp',
           'Silkworm', 'Silverfish', 'Skink', 'Skunk', 'Sloth', 'Slug', 'Smelt', 'Snail', 'Snake',
           'Snipe', 'Sole', 'Sparrow', 'Spider', 'Spoonbill', 'Squid', 'Squirrel', 'Starfish',
           'Stingray', 'Stoat', 'Stork', 'Sturgeon', 'Swallow', 'Swan', 'Swift', 'Swordfish',
           'Swordtail', 'Tahr', 'Takin', 'Tapir', 'Tarantula', 'Tarsier', 'Termite', 'Tern', 'Thrush',
           'Tick', 'Tiger', 'Tiglon', 'Toad', 'Tortoise', 'Toucan', 'Trout', 'Tuna', 'Turkey',
           'Turtle', 'Tyrannosaurus', 'Urial', 'Vicuna', 'Viper', 'Vole', 'Vulture', 'Wallaby',
           'Walrus', 'Wasp', 'Warbler', 'Weasel', 'Whale', 'Whippet', 'Whitefish', 'Wildcat',
           'Wildebeest', 'Wildfowl', 'Wolf', 'Wolverine', 'Wombat', 'Woodpecker', 'Worm', 'Wren',
           'Xerinae', 'Yak', 'Zebra', 'Alpaca', 'Cat', 'Cattle', 'Chicken', 'Dog', 'Donkey', 'Ferret',
           'Gayal', 'Goldfish', 'Guppy', 'Horse', 'Koi', 'Llama', 'Sheep', 'Yak']

## Utilizing Google Gemini 1.5-falsh model ##
model = genai.GenerativeModel("gemini-1.5-flash")

## API key necessary for authentication and prompt generation ##
genai.configure(api_key="AIzaSyCRhR2AhI9DIkbFsLdg8p30jyxOYczkPw8")

## Dictionary to keep track of original variable names and their changed values ##
existing_vars = dict()

## Creation of subclass derived from CSTTransformer which allows modified traversal attributes ##
class VarRename(cst.CSTTransformer):

    ## Allows access to parent node metadata ##
    METADATA_DEPENDENCIES = (ParentNodeProvider,)

    ############ Function to generate a new synonym for the existing variable using gemini API ############

    def get_synonym(self, original_varname):

        ## Only rename the variable if Gemini has not come up with a synonym for it. Otherwise return the current synonym ##
        if original_varname not in existing_vars:

            try:

                ## Creation of prompt for provided original variable name ##
                synonym = model.generate_content(f"Provide a one-word synonym for '{original_varname}' in a coding context. Also make it lower case or camel-case. Make it unique, different, and distinct. [{random.randint(0, 10000)}. Please answer with only the wrod and nothing more.]")

                ## Parse the API return value to extract the reponse as text ##
                synonym = synonym.text
                synonym = re.sub(r"[^a-zA-Z0-9_]", "", synonym)

                ## Add key-value pair to the dictionary if it does not exist already ##
                existing_vars[original_varname] = synonym

            except Exception as e:

                print(f"Error fetching synonym for '{original_varname}', using animal name placeholder.")
                #print(f"Error fetching synonym for '{original_varname}':", e)
                #existing_vars[original_varname] = original_varname
                new_name=random.choice(animals)
                animals.remove(new_name)
                animals.append(str(new_name+str(1)))
                existing_vars[original_varname] = new_name

        return existing_vars[original_varname]
    #######################################################################################################



    ######################### Function for transforming the 'Param' type Name nodes #######################

    # Context for function: Variable is present within a functiondef or call. ( Ex: function(variable1, variable2) ).

    def leave_Param(self, original_node: cst.Param, updated_node: cst.Param) -> cst.Param:

        if isinstance(updated_node.name, cst.Name):

            new_varname = self.get_synonym(updated_node.name.value)
            updated_node = updated_node.with_changes(name=updated_node.name.with_changes(value=new_varname))

        return updated_node
    #######################################################################################################



    ######################### Function for transforming the 'For' type Name nodes #########################

    # Context for function: Variable is present within a For statement as a target or iter value. #
    # (Ex: for variable in variable2:)

    def leave_For(self, original_node: cst.For, updated_node: cst.For) -> cst.For:

        if isinstance(updated_node.target, cst.Name):

            new_varname = self.get_synonym(updated_node.target.value)
            updated_node = updated_node.with_changes(target=updated_node.target.with_changes(value=new_varname))

        elif isinstance(updated_node.target, cst.Tuple):

              updated_tuple = updated_node.target

              for i, element in enumerate(updated_tuple.elements):

                  if isinstance(element.value, cst.Name):

                      new_varname = self.get_synonym(element.value.value)
                      new_element = element.with_changes(value=element.value.with_changes(value=new_varname))
                      updated_tuple = updated_tuple.with_changes(elements=tuple(updated_tuple.elements[:i]) + (new_element,) + tuple(updated_tuple.elements[i+1:]))

              updated_node = updated_node.with_changes(target=updated_tuple)

        if isinstance(updated_node.iter, cst.Name):

            new_varname = self.get_synonym(updated_node.iter.value)
            updated_node = updated_node.with_changes(iter=updated_node.iter.with_changes(value=new_varname))

        return updated_node
    #######################################################################################################



    ######################### Function for transforming the 'AssignTarget' type Name nodes ################

    # Context for function: Left target value of an assignment operator. (Ex: variable = 5).

    def leave_AssignTarget(self, original_node: cst.AssignTarget, updated_node: cst.AssignTarget) -> cst.AssignTarget:

        if isinstance(updated_node.target, cst.Name):

            new_varname = self.get_synonym(updated_node.target.value)
            updated_node = updated_node.with_changes(target=updated_node.target.with_changes(value=new_varname))


        return updated_node
    #######################################################################################################



    ######################### Function for transforming the 'Attribute' type Name nodes ###################

    # Context for function:

    def leave_Attribute(self, original_node: cst.AssignTarget, updated_node: cst.AssignTarget) -> cst.AssignTarget:

        if isinstance(updated_node.value, cst.Name) and updated_node.value.value in existing_vars:

            new_varname = self.get_synonym(updated_node.value.value)
            return updated_node.with_changes(value=updated_node.value.with_changes(value=new_varname))

        return updated_node
    #######################################################################################################



    ######################### Function for transforming the 'Arg' type Name nodes #########################

    # Context for function:

    def leave_Arg(self, original_node: cst.Arg, updated_node: cst.Arg) -> cst.Arg:

        if isinstance(updated_node.value, cst.Name):

            new_varname = self.get_synonym(updated_node.value.value)
            return updated_node.with_changes(value=updated_node.value.with_changes(value=new_varname))

        return updated_node
    #######################################################################################################


    '''
    ######################### Function for transforming the 'ImportAlias' type Name nodes #################

    # Context for function:

    def leave_ImportAlias(self, original_node: cst.ImportAlias, updated_node: cst.ImportAlias) -> cst.ImportAlias:
        alias_node = updated_node.asname
        if alias_node and alias_node.name.value:
            new_alias = self.get_synonym(alias_node.name.value)
            return updated_node.with_deep_changes(alias_node.name, value=new_alias)
        return updated_node
    #######################################################################################################
    '''

    ######################### Function for transforming the 'BinaryOperation' type Name nodes #############

    # Context for function:

    def leave_BinaryOperation(self, original_node: cst.BinaryOperation, updated_node: cst.BinaryOperation) -> cst.BinaryOperation:

        if isinstance(updated_node.left, cst.Name):

            new_left_varname = self.get_synonym(updated_node.left.value)
            updated_node = updated_node.with_changes(left=updated_node.left.with_changes(value=new_left_varname))

        if isinstance(updated_node.right, cst.Name):

            new_right_varname = self.get_synonym(updated_node.right.value)
            updated_node = updated_node.with_changes(right=updated_node.right.with_changes(value=new_right_varname))

        return updated_node
    #######################################################################################################


    '''
    ######################### Function for transforming the 'AsName' type Name nodes ######################

    # Context for function:

    def leave_AsName(self, original_node: cst.AsName, updated_node: cst.AsName) -> cst.AsName:

        if isinstance(updated_node.name, cst.Name):

            new_varname = self.get_synonym(updated_node.name.value)
            updated_node = updated_node.with_changes(name=updated_node.name.with_changes(value=new_varname))

        return updated_node
    #######################################################################################################
    '''


    ######################### Function for transforming the 'Comparison' type Name nodes ##################

    # Context for function:

    def leave_Comparison(self, original_node: cst.Comparison, updated_node: cst.Comparison) -> cst.Comparison:

        if isinstance(updated_node.left, cst.Name):

            new_left_varname = self.get_synonym(updated_node.left.value)
            updated_node = updated_node.with_changes(left=updated_node.left.with_changes(value=new_left_varname))

        return updated_node
    #######################################################################################################



    ######################### Function for transforming the 'Return' type Name nodes #######################

    # Context for function:

    def leave_Return(self, original_node: cst.Return, updated_node: cst.Return) -> cst.Return:

        if isinstance(updated_node.value, cst.Name):

            new_varname = self.get_synonym(updated_node.value.value)
            updated_node = updated_node.with_changes(value=updated_node.value.with_changes(value=new_varname))

        return updated_node
    #######################################################################################################
    
    
    def leave_FormattedString(self, original_node: cst.FormattedString, updated_node: cst.FormattedString) -> cst.FormattedString:

        new_parts = []

        for part in updated_node.parts:

            if isinstance(part, cst.FormattedStringExpression):

                if isinstance(part.expression, cst.Name):

                    new_varname = self.get_synonym(part.expression.value)
                    new_part = part.with_changes(expression=part.expression.with_changes(value=new_varname))
                    new_parts.append(new_part)

                else:

                    new_parts.append(part)
            else:

                new_parts.append(part)

        # Update the formatted string with the modified parts
        return updated_node.with_changes(parts=new_parts)

## Provides extra data for every node in the tree ##
wrapped_module = MetadataWrapper(original_cst)
## Traverse tree with transformer subclass ##
vars_renamed = wrapped_module.visit(VarRename())
print("Variables renamed...")


'''
Rename Functions

'''
# placeholder list to replace function names with
colors = ['aliceblue','antiquewhite','aqua','aquamarine','azure','beige','bisque','black','blanchedalmond',
          'blue','blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue',
          'cornsilk','crimson','cyan','darkblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki',
          'darkmagenta','darkolivegreen','darkorange','darkorchid','darkred','darksalmon','darkseagreen',
          'darkslateblue','darkslategray','darkturquoise','darkviolet','deeppink','deepskyblue','dimgray',
          'dodgerblue','firebrick','floralwhite','forestgreen','fuchsia','gainsboro','ghostwhite','gold','goldenrod',
          'gray','green','greenyellow','honeydew','hotpink','indianred','indigo','ivory','khaki','lavender',
          'lavenderblush','lawngreen','lemonchiffon','lightblue','lightcoral','lightcyan','lightgoldenrodyellow',
          'lightgreen','lightgray','lightpink','lightsalmon','lightseagreen','lightskyblue','lightslategray',
          'lightsteelblue','lightyellow','lime','limegreen','linen','magenta','maroon','mediumaquamarine','mediumblue',
          'mediumorchid','mediumpurple','mediumseagreen','mediumslateblue','mediumspringgreen','mediumturquoise',
          'mediumvioletred','midnightblue','mintcream','mistyrose','moccasin','navajowhite','navy','oldlace','olive',
          'olivedrab','orange','orangered','orchid','palegoldenrod','palegreen','paleturquoise','palevioletred',
          'papayawhip','peachpuff','peru','pink','plum','powderblue','purple','red','rosybrown','royalblue','saddlebrown',
          'salmon','sandybrown','seagreen','seashell','sienna','silver','skyblue','slateblue','slategray','snow',
          'springgreen','steelblue','tan','teal','thistle','tomato','turquoise','violet','wheat','white','whitesmoke'
          ,'yellow','yellowgreen']

#dict of existing pairs, will be used to replace all calls of old function with calls to new name
# assuming that multiple funcs don't have the same new name
func_name_pairs = dict()

# rename all function defs or aliases (only rename custom functions, not things like print() or math.log)
class FuncRename(cst.CSTTransformer):

  # rename function names in a "def funcname: " node
  # FunctionDef node docs: (https://libcst.readthedocs.io/_/downloads/en/latest/pdf/#page=73&zoom=auto,-205,215)
  def leave_FunctionDef(self, node: cst.FunctionDef, updated_node: cst.FunctionDef) -> cst.FunctionDef:
    if updated_node.name.value not in func_name_pairs:
      new_name=random.choice(colors)
      colors.remove(new_name)
      colors.append(str(new_name+str(1)))
      func_name_pairs.update({updated_node.name.value: new_name})
    # the name node in function def is a child node, thus to change function name via the FunctionDef parent node, use with_deep_changes via:
    # (https://libcst.readthedocs.io/en/latest/nodes.html#libcst.CSTNode.with_deep_changes)

    #print("Function def of \'"+updated_node.name.value+"\' has been renamed to \'"+func_name_pairs[updated_node.name.value]+"\'")
    return updated_node.with_deep_changes(updated_node.name, value=func_name_pairs[updated_node.name.value])

  # rename function names in a "import x as y" node
  # ImportAlias node docs: (https://libcst.readthedocs.io/_/downloads/en/latest/pdf/#page=78&zoom=auto,-205,314)
  def leave_ImportAlias(self, node: cst.ImportAlias, updated_node: cst.ImportAlias) -> cst.ImportAlias:
    alias_node=updated_node.asname
    if alias_node:
      if alias_node.name.value not in func_name_pairs:
        new_name=random.choice(colors)
        colors.remove(new_name)
        colors.append(str(new_name+str(1)))
        func_name_pairs.update({alias_node.name.value: new_name})

      #print("Import alias of \'"+alias_node.name.value+"\' has been renamed to \'"+func_name_pairs[alias_node.name.value]+"\'")
      return updated_node.with_deep_changes(updated_node.asname.name, value=func_name_pairs[alias_node.name.value])
    return updated_node


# kept separate from FuncRename to do two-pass and prevent renaming predefined functions like print()
class CallRename(cst.CSTTransformer):

  # rename function names in a function call node
  # Call node docs: (https://libcst.readthedocs.io/_/downloads/en/latest/pdf/#page=53&zoom=auto,-205,721)
  def leave_Call(self, node: cst.Call, updated_node: cst.Call) -> cst.Call:

    # Name node: (https://libcst.readthedocs.io/_/downloads/en/latest/pdf/#page=48&zoom=auto,-205,344)
    if (type(updated_node.func)) is cst._nodes.expression.Name:
      if (updated_node.func.value) in func_name_pairs:

        #print("Function call of \'"+updated_node.func.value+"\' has been renamed to \'"+func_name_pairs[updated_node.func.value]+"\'")
        return updated_node.with_deep_changes(updated_node.func, value=func_name_pairs[updated_node.func.value])

    # for attributes, aka package.function(), only the package can be potentially custom (e.g. 'import math as blah', 'blah.log()')
    # as if you import a subsect and rename it, it will be a normal function call (e.g. 'from math import log as blah', funct call would be
    #                                                                                   'blah()' not 'math.blah()'
    # Attribute node: (https://libcst.readthedocs.io/_/downloads/en/latest/pdf/#page=48&zoom=auto,-205,344)
    elif (type(updated_node.func)) is cst._nodes.expression.Attribute:
      if updated_node.func.value.value in func_name_pairs:

        #print("Function call of \'"+updated_node.func.value.value+"."+updated_node.func.attr.value+"\' has been renamed to \'"+func_name_pairs[updated_node.func.value.value]+"."+updated_node.func.attr.value+"\'")
        return updated_node.with_deep_changes(updated_node.func.value, value=func_name_pairs[updated_node.func.value.value])
    return updated_node


funcs_renamed=vars_renamed.visit(FuncRename())
print("Functions renamed...")
func_calls_renamed=funcs_renamed.visit(CallRename())
print("Function calls renamed...")

'''
Save final edited source code into Python file

'''

#modified_code=transformed_cst.code
modified_code=func_calls_renamed.code

## Write the newly modified code to a new file ##
output_filename = str(str(path.stem)+"_RENAMED.py")
with open(output_filename, "w") as output_file:
    output_file.write(modified_code)
output_file.close()
print(f"Output generated, look for {output_filename} in current directory.")





