import random
import numpy as np
import os
import numpy as np
import logging

import sys
np.set_printoptions(threshold=sys.maxsize)
import time
from pyface.qt import QtCore, QtGui
from PIL import Image as im
from traits.api import Bool, Float
from traitsui.api import BasicEditorFactory
from traitsui.qt4.editor import Editor
from traitsui.qt4.image_editor import QImageView

from traits.api import (
    Either,
    Enum,
    HasRequiredTraits,
    Int,
    Array,
    Bool,
    Color,
    Dict,
    Directory,
    Float,
    Instance,
    List,
    on_trait_change,
    Range,
    Tuple,
    Unicode,
)

from traits.api import Instance, Button
from traitsui.api import (
    EnumEditor,
    HGroup,
    HSplit,
    Item,
    ModelView,
    ObjectColumn,
    TableEditor,
    TextEditor,
    UItem,
    VGroup,
    View,
    VSplit,
)


from scipy.ndimage import convolve

DEFAULT_MASK_DIRECTORY = 'masks'
LIFE = "Life"
DEATH = "Death"
PASS = "Pass"
BOTH = "Both"
RANDOM = "Random"
ZEROS = "Zeros"

final_list = []


def load_masks(dir_name):
    """
    Loads masks from a target directory and returns a dict of name: mask
    usage: load_mask("mask_directory")
    """


    masks = {}
    for mask_name in os.listdir(dir_name):
        with open(os.path.join(dir_name, mask_name), "r") as f:
            mask = [[int(n) for n in line.split()] for line in f.readlines()]
            masks[mask_name] = np.array(mask, ndmin=2)

    return masks


# Conditions for a rule to be a "Rule" for our MNCA
class Rule(HasRequiredTraits):
    # Mask the rule applies to
    mask = Unicode(required=True)

    #: Whether this rule acts on living or dead cells, or both
    acts_on = Enum(BOTH, (1, 0, BOTH))

    #: Rule limits (inclusive!), or None if there is no bound
    #: TODO: limits should match dtype if we want continuous MNCAs
    lower_limit = Either(Int, None, required=True)
    upper_limit = Either(Int, None, required=True)

    result = Enum(LIFE, DEATH, required=True)



# There are other masks available that can be used from masks folder - sanyam
DEFAULT_BRUSH = np.array(
  [
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
    ],
)
import deflate



import cv2
import numpy as np
import glob







from natsort import natsorted, ns



import matplotlib.pyplot as plt
import numpy as np
import random

from PIL import ImageDraw

import numpy as np
from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

deflate_values = []
from evolutionary_computation import EvolutionaryComputation
class MncaModel(HasRequiredTraits):

    #: Board size (X, Y)
    board_size = Tuple(Range(1, 500), Range(1, 500), required=True)

    #: % of living cells on reset
    # reset_life_pct = Float(Range(0, 1))
    reset_life_pct = Float(0.56)

    evolve_count = Int(500)

    #: Board for the MNCA
    board = Array(shape=(None, None))

    #: Directory to parse masks from
    masks_dir = Directory(DEFAULT_MASK_DIRECTORY, exists=True)

    #: Available masks (name to array)
    masks = Dict(Unicode, Array(shape=(None, None)))

    #: Rules
    rules = List(Instance(Rule), required=False)

    #: Pause updating the model
    paused = Bool(False)

    #: Drawing brush
    brush = Array(shape=(None, None), value=DEFAULT_BRUSH)

    live_color = Color("white")
    dead_color = Color("black")

    @on_trait_change("masks_dir")
    def set_masks(self):
        self.masks = load_masks(self.masks_dir)
        self.randomize_rules()

    def _masks_default(self):
        # TODO: this is a bit hacky to help with traits init of this class
        return load_masks(DEFAULT_MASK_DIRECTORY)

    @on_trait_change("board_size")
    def reset_board(self):
        self.board = np.ones(self.board_size, dtype=int)
        self.board_reset()

    @on_trait_change("rules[]")
    def print_new_rules(self):
        print("----------")
        for rule in self.rules:
            print(
                "mask='{rule.mask}', "
                "acts_on={rule.acts_on!r}, "
                "lower_limit={rule.lower_limit}, "
                "upper_limit={rule.upper_limit}, "
                "result={rule.result})".format(rule=rule)
            )
            
            # rule_set = ("mask='{rule.mask}', "+"acts_on={rule.acts_on!r}, "+"lower_limit={rule.lower_limit}, "+"upper_limit={rule.upper_limit}, "+"result={rule.result})").format(rule=rule)
            # logging.basicConfig(filename="std.log", 
            #                     format='%(asctime)s %(message)s', 
            #                     filemode='a') 

            # logger=logging.getLogger() 
            # logger.setLevel(logging.DEBUG) 
            # logger.debug(rule_set)
            # # logger.debug("-----------------")


    def board_reset(self):
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                self.board[i, j] = 1 if random.random() < self.reset_life_pct else 0

    def clear_board(self, value=0):
        self.board[:, :] = value

    def draw(self, target):
        """
        Draw on the board using the current brush at the target coordinates
        """
        for offset in np.transpose(np.where(self.brush)):
            offset -= np.array(self.brush.shape) // 2
            coord = target + offset
            if coord[0] < self.board.shape[0] and coord[1] < self.board.shape[1]:
                self.board[coord[0], coord[1]] = 1

    


    def evolve_board(self):
        """
        Evolve the board one step according to the rules
        and save as image
        # """
        self.evolve_count = self.evolve_count - 1
        # print(self.evolve_count)
        # evolve_count = evolve_count-1
        # ts = time.time()
        # save array as image
        board_array = self.board
        # print(board_array)
        # board_array = (board_array*255).astype(np.uint8)
        # data = im.fromarray(board_array)
        # data.save(str(ts).replace('.','')+'.png')
        # final_list.append(board_array)
        
        with open("board_arrays.txt", "w") as output:
            output.write(str(board_array))
        filedata = open('board_arrays.txt', "rb").readline()
        compressed = deflate.gzip_compress(filedata, 6)
        deflate_size = compressed.__sizeof__()

        # Convert board array to image
        # board_array = board_array * 255
        # print(board_array)
        data = im.fromarray(np.array(board_array*255).astype(np.uint8))
        data.save(str(self.evolve_count)+'.png')
        

        # # Now just open the image and add text and save it back!

        # img = im.open(str(self.evolve_count)+'.png')
        # I1 = ImageDraw.Draw(img)
        # I1.text((10, 60), 'iteration: '+str(self.evolve_count), fill='red')
        # img.save(str(self.evolve_count)+'.png')
        
        if(self.evolve_count==0):
            

            # Save all images in the folder to another folder
            # and make a video out of it
            ts = time.time()
            os.mkdir("outputs"+str(ts))
            os.system("mv *.png outputs"+str(ts))
            os.chdir("outputs"+str(ts))
            # os.system('ffmpeg -framerate 2 -pattern_type glob -i "*.png" output.avi')
            

            frameSize = (500, 500)
            out = cv2.VideoWriter('final_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, frameSize)
            file_list = [img for img in os.listdir('.')]

            print("Before: ",file_list)
            file_list = natsorted(file_list, key=lambda y: y.lower(),reverse=True)
            print("After: ",file_list)
            for filename in file_list:
                img = cv2.imread(filename)
                out.write(img)
            

            # PLOT DEFLATE CHART!

            data = deflate_values
            plt.plot(data, color='magenta', marker='o',mfc='pink' ) #plot the data
            plt.xticks(range(0,len(data)+1, 1)) #set the tick frequency on x-axis
            plt.ylabel('Deflate Vlaue') #set the label for y axis
            plt.xlabel('index') #set the label for x-axis
            plt.title("Plotting a list") #set the title of the graph
            plt.show() #display the graph
            # data = np.array(deflate_values)
            # sns.distplot(data,bins="doane",kde=False,hist_kws={"align" : "right"})
            # plt.show()
            plt.savefig("deflate_chart.png")
            
            os.system('mv -v /home/sanyam/Desktop/my_mnca_deflate_EC/std.log /home/sanyam/Desktop/my_mnca_deflate_EC/outputs'+str(ts))
            os.system('mv -v /home/sanyam/Desktop/my_mnca_deflate_EC/board_arrays.txt /home/sanyam/Desktop/my_mnca_deflate_EC/outputs'+str(ts))


            sys.exit()
        
        
        
        if self.paused:
            return

        # TODO: update this in another thread if possible, to stop the UI from juttering

        gridmask = np.ones_like(self.board)
        convgrid = np.zeros_like(self.board)

        # Where the lower and upper bounds of the rule are satisfied
        rule1 = np.ones_like(self.board)
        rule2 = np.ones_like(self.board)

        # We pass initial random rules from the main class, however, 
        # we generate and evolve the rules from Genetic algorithm and over ride the previous rules
        # This will result similar deflate values (orderly) and we will have best generation at the end of evolution
        
        print("RULES BEFORE STARTING")
        print("RULES BEFORE STARTING")
        print("RULES BEFORE STARTING")
        list_of_rules = [[rulee.lower_limit,rulee.upper_limit,rulee.result] for rulee in self.rules]
        print(list_of_rules)
        
        # I am trying to update the rules from list to traitobject 
        # [[8, 2, 'Life'], [5, 1, 'Life'], [1, 2, 'Death'], [4, 8, 'Life']]
        
        # This list has to be evolved by EC
        # This list has to be evolved by EC
        # This list has to be evolved by EC
        # This list has to be evolved by EC
        ec_list = list_of_rules
        # This list has to be evolved by EC
        # This list has to be evolved by EC
        # This list has to be evolved by EC
        # This list has to be evolved by EC
        # example - Evolve(previous list)
        # from evolutionary_conputation import EvolutionaryComputation
        ec_list = EvolutionaryComputation(ec_list,deflate_size)




        
        i=0
        for rulese in self.rules: 
            for eachrulevalue in range(3):
                rulese.lower_limit = ec_list[i][0]
                rulese.upper_limit = ec_list[i][1]
                rulese.result = ec_list[i][2]
            i=i+1
        print("RULES AFTER START & CURRENT EVOLUTION")
        print("RULES AFTER START & CURRENT EVOLUTION")
        print("RULES AFTER START & CURRENT EVOLUTION")
        list_of_rules = [[rulese.lower_limit,rulese.upper_limit,rulese.result] for rulese in self.rules]
        print(list_of_rules)
        

        # rule_set_evolved = ("mask='{rule.mask}', "+"acts_on={rule.acts_on!r}, "+"lower_limit={rule.lower_limit}, "+"upper_limit={rule.upper_limit}, "+"result={rule.result})").format(rule=rule)

        #now we will Create and configure logger 
        logging.basicConfig(filename="std.log", 
                            format='%(asctime)s %(message)s', 
                            filemode='a') 
        
        logger=logging.getLogger()
        
        logger.setLevel(logging.DEBUG) 
        # logger.debug("-----------------")
        # logger.debug(rule_set_evolved)
        logger.debug("-----------------")

        for rule in self.rules:
            # print(
            #     "mask='{rule.mask}', "
            #     "acts_on={rule.acts_on!r}, "
            #     "lower_limit={rule.lower_limit}, "
            #     "upper_limit={rule.upper_limit}, "
            #     "result={rule.result})".format(rule=rule)
            # )
            
            rule_set = ("mask='{rule.mask}', "+"acts_on={rule.acts_on!r}, "+"lower_limit={rule.lower_limit}, "+"upper_limit={rule.upper_limit}, "+"result={rule.result})").format(rule=rule)
            logging.basicConfig(filename="std.log", 
                                format='%(asctime)s %(message)s', 
                                filemode='a') 

            logger=logging.getLogger() 
            logger.setLevel(logging.DEBUG) 
            logger.debug(rule_set)
        

        with open("board_arrays.txt", "w") as output:
            output.write(str(board_array))
        filedata = open('board_arrays.txt', "rb").readline()
        compressed = deflate.gzip_compress(filedata, 6)
        deflate_size = compressed.__sizeof__()
        # print("Rules used: ",)
        print("Deflate Size: ",deflate_size)
        
        #now we will Create and configure logger 
        # logging.basicConfig(filename="std.log", 
        #                     format='%(asctime)s %(message)s', 
        #                     filemode='a') 
        
        # logger=logging.getLogger()
        
        # logger.setLevel(logging.DEBUG) 
        
        logger.debug("-----------------") 
        logger.debug(deflate_size)
        # logger.debug("-----------------")
        deflate_values.append(deflate_size)
        
        
        img = im.open(str(self.evolve_count)+'.png')
        I1 = ImageDraw.Draw(img)
        I1.text((10, 60), 'Iter No. '+str(self.evolve_count)+', deflate_size: '+str(deflate_size), fill='red')
        img.save(str(self.evolve_count)+'.png')
        
        
        print("------------------------ONE ITERNATION FINISHED------------------------")
        for rule in self.rules:
            if not gridmask.any():
                break
            convolve(self.board, self.masks[rule.mask], mode="wrap", output=convgrid)
            if rule.lower_limit is not None:
                rule1 = np.where(convgrid >= rule.lower_limit, 1, 0)
            else:
                rule1[:] = 1

            if rule.upper_limit is not None:
                rule2 = np.where(convgrid <= rule.upper_limit, 1, 0)
            else:
                rule2[:] = 1

            slc = (rule1 & rule2 & gridmask)

            if rule.acts_on != BOTH:
                acts_on = np.where(self.board == rule.acts_on, 1, 0)
                slc &= acts_on

            self.board[np.where(slc)] = 1 if rule.result == LIFE else 0
            gridmask[np.where(slc)] = 0

           























class _BoolArrayEditor(Editor):

    drawing = Bool

    def init(self, parent):
        self.control = QImageView()
        self._widget = QtGui.QWidget()

        self.drawing = False

        self.control.mousePressEvent = self.set_drawing
        self.control.mouseReleaseEvent = self.unset_drawing
        self.control.mouseMoveEvent = self.draw_pixel

        self.update_editor()

        # Set up timed events
        self._widget.timer = QtCore.QTimer()
        self._widget.timer.start(self.factory.update_ms)
        self._widget.timer.timeout.connect(self.object.evolve_board)
        self._widget.timer.timeout.connect(self.update_editor)

    def set_drawing(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
        self.draw_pixel(event)

    def unset_drawing(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = False

    def draw_pixel(self, event):
        x = event.pos().x()
        y = event.pos().y()

        self.object.draw(np.array([y, x]))

    def update_editor(self):
        img = QtGui.QImage(
            self.object.board.astype(np.int8).data,
            self.object.board_size[1],
            self.object.board_size[0],
            QtGui.QImage.Format_Indexed8
        )
        img.setColorTable([self.object.dead_color.rgb(), self.object.live_color.rgb()])
        self.control.setPixmap(QtGui.QPixmap.fromImage(img))


class BoolArrayEditor(BasicEditorFactory):

    scale = Bool
    allow_upscaling = Bool
    preserve_aspect_ratio = Bool
    allow_clipping = Bool

    update_ms = Float(60/500)

    klass = _BoolArrayEditor


def optional_int_editor():
    return TextEditor(
        evaluate=lambda x: int(x) if x != "" else None,
        format_func=lambda x: str(x) if x is not None else "",
    )


class MncaView(ModelView):

    model = Instance(MncaModel, allow_none=False)

    randomize_rules = Button("Randomize Rules")

    def _randomize_rules_fired(self):
        self.model.randomize_rules()

    reset_board = Button("Reset Board")

    def _reset_board_fired(self):
        self.model.reset_board()

    clear_board = Button("Clear Board")

    def _clear_board_fired(self):
        self.model.clear_board()

    def rules_table(self):
        return TableEditor(
            sortable=False,
            auto_size=True,
            orientation="vertical",
            edit_view=View(
                Item("mask", editor=EnumEditor(values=sorted(self.model.masks.keys()))),
                Item("lower_limit", editor=optional_int_editor()),
                Item("upper_limit", editor=optional_int_editor()),
                Item("acts_on"),
                Item("result"),
            ),
            # columns=[
            #     ObjectColumn(
            #         name="mask",
            #         label="Mask",
            #         editable=False,
            #     ),
            #     ObjectColumn(
            #         name="lower_limit",
            #         label="Lower",
            #         editable=False,
            #     ),
            #     ObjectColumn(
            #         name="upper_limit",
            #         label="Upper",
            #         editable=False,
            #     ),
            #     ObjectColumn(
            #         name="acts_on",
            #         label="Acts On",
            #         editable=False,
            #     ),
            #     ObjectColumn(
            #         name="result",
            #         label="Result",
            #         editable=False,
            #     )
            # ]
        )

    def default_traits_view(self):
        view = View(
            HSplit(
                VGroup(
                    UItem(
                        "model.board",
                        editor=BoolArrayEditor(
                            scale=True,
                            allow_upscaling=False,
                            allow_clipping=False,
                            preserve_aspect_ratio=True,
                        ),
                        resizable=True,
                        springy=True,
                    ),
                    HGroup(
                        # Item("model.live_color", label="Life Colour"),
                        # Item("model.dead_color", label="Dead Colour"),
                    ),
                ),
                VSplit(
                    # VGroup(
                    #     Item("model.paused", label="Pause"),
                    #     Item("model.board_size"),
                    # ),
                    VGroup(
                        # Item("model.reset_life_pct", label="Reset Life %"),
                        # UItem("reset_board"),
                        # UItem("clear_board"),
                    )
                ),
                VGroup(
                    # Item("model.masks_dir", label="Masks Dir"),
                    # UItem("model.rules", editor=self.rules_table()),
                    # UItem("randomize_rules"),
                ),
                springy=True,
            ),
            resizable=True,
        )
        return view






# Driving Code:

# # Uncomment whichever rule you wanna use
# rule_list = [
#             Rule(mask="mask_a.txt", lower_limit=3, upper_limit=7, result=DEATH),
#             Rule(mask="8_neighbor.txt", lower_limit=2, upper_limit=5, result=DEATH),
#             Rule(mask="plus_1w1l.txt", lower_limit=1, upper_limit=1, result=DEATH),
#             Rule(mask="plus_1w1l.txt", lower_limit=1, upper_limit=4, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=6, upper_limit=9, result=LIFE),
#             Rule(mask="plus_1w2l.txt", lower_limit=1, upper_limit=5, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=0, upper_limit=7, result=DEATH),
#             Rule(mask="9_neighbor.txt", lower_limit=1, upper_limit=4, result=LIFE),
#             Rule(mask="8_neighbor.txt", lower_limit=6, upper_limit=8, result=DEATH),]
            


# rule_list = [
#             # B3/S23 - keep reset_life_pct as 0.8 in line 114 of this program
#             Rule(mask="9_neighbor.txt", lower_limit=0, upper_limit=1, result=DEATH),
#             Rule(mask="9_neighbor.txt", lower_limit=3, upper_limit=3, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=4, upper_limit=8, result=DEATH),
#             Rule(mask="9_neighbor.txt", lower_limit=2, upper_limit=3, result=LIFE)
#             ]


# rule_list = [
#             # B1357/S1357 REPLICATOR RULE - keep reset_life_pct as 0.99999
#             Rule(mask="9_neighbor.txt", lower_limit=0, upper_limit=1, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=2, upper_limit=3, result=DEATH),
#             Rule(mask="9_neighbor.txt", lower_limit=4, upper_limit=5, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=6, upper_limit=7, result=DEATH),
#             Rule(mask="9_neighbor.txt", lower_limit=1, upper_limit=2, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=3, upper_limit=4, result=DEATH),
#             Rule(mask="9_neighbor.txt", lower_limit=5, upper_limit=6, result=LIFE),
#             Rule(mask="9_neighbor.txt", lower_limit=7, upper_limit=8, result=DEATH)
#             ]

# rule_list = [
#             # LARGR THAN LIFE - keep reset_life_pct as 0.42
#             Rule(mask="11x11_larger_than_life.txt", lower_limit=0, upper_limit=33, acts_on= 1,result=DEATH),
#             Rule(mask="11x11_larger_than_life.txt", lower_limit=34, upper_limit=45, acts_on= 0,result=LIFE),
#             Rule(mask="11x11_larger_than_life.txt", lower_limit=58, upper_limit=121, acts_on= 1, result=DEATH)
#             ]


# using mask_a.txt for MNCA with 6 update functions from - 
# https://slackermanz.com/understanding-multiple-neighborhood-cellular-automata/
# keep reset_life_pct as 0.5
# Originally they use averages, but using approximation for lower limit and upper limit

# rule_list = [
#             Rule(mask="mask_a.txt", lower_limit=int(0.210*225), upper_limit=int(0.220*225),result=LIFE),
#             Rule(mask="mask_a.txt", lower_limit=int(0.350*225), upper_limit=int(0.500*225),result=DEATH),
#             Rule(mask="mask_a.txt", lower_limit=int(0.750*225), upper_limit=int(0.850*225),result=DEATH),
#             Rule(mask="mask_a.txt", lower_limit=int(0.100*225), upper_limit=int(0.280*225),result=DEATH),
#             Rule(mask="mask_a.txt", lower_limit=int(0.430*225), upper_limit=int(0.550*225),result=LIFE),
#             Rule(mask="mask_a.txt", lower_limit=int(0.120*225), upper_limit=int(0.150*225),result=DEATH),
#             ]


# using mask_d.txt for MNCA with 6 update functions from - 
# https://slackermanz.com/understanding-multiple-neighborhood-cellular-automata/
# keep reset_life_pct as 0.5
# Originally they use averages, but using approximation for lower limit and upper limit

# # # This rule works well but very slow :/
# rule_list = [
#             Rule(mask="mask_d.txt", lower_limit=int(0.210*225), upper_limit=int(0.220*225),result=LIFE),
#             Rule(mask="mask_d.txt", lower_limit=int(0.350*225), upper_limit=int(0.500*225),result=DEATH),
#             Rule(mask="mask_d.txt", lower_limit=int(0.750*225), upper_limit=int(0.850*225),result=DEATH),
#             Rule(mask="mask_d.txt", lower_limit=int(0.100*225), upper_limit=int(0.280*225),result=DEATH),
#             Rule(mask="mask_d.txt", lower_limit=int(0.430*225), upper_limit=int(0.550*225),result=LIFE),
#             Rule(mask="mask_d.txt", lower_limit=int(0.120*225), upper_limit=int(0.150*225),result=DEATH),
#             ]


# Known interesting rule - GoL

life_or_death = [LIFE, DEATH]
neighborhoods = [0,1,2,3,4,5,6,7,8]


rule_list_before = [random.choice(neighborhoods),
                    random.choice(neighborhoods),
                    random.choice(life_or_death),
                    random.choice(neighborhoods),
                    random.choice(neighborhoods),
                    random.choice(life_or_death),
                    random.choice(neighborhoods),
                    random.choice(neighborhoods),
                    random.choice(life_or_death),
                    random.choice(neighborhoods),
                    random.choice(neighborhoods),
                    random.choice(life_or_death)]

# rule_list_before = [0,1,LIFE,4,4,DEATH,4,7,DEATH,2,1,LIFE]

# numerical values lies between 0 to 8

# Running one 500 runs will save 500 board patterns to a file.

# Evolutionary Algorithm Module - Lets try with very basic GoL based EA where we find interstingness on the basis of DEFALTE of the array


# # calculate deflate
# import deflate
# def calculate_deflate(filepath):
#     level=6

#     filedata = open(filepath, "r").readline()
#     compressed = deflate.gzip_compress(filedata, level)
#     deflate_size = compressed.__sizeof__()
#     return deflate_size


# deflate_value = calculate_deflate('board_arrays.txt')

# print(deflate_value)






rule_list = [
                Rule(mask='9_neighbor.txt',lower_limit=rule_list_before[0],upper_limit=rule_list_before[1],result=rule_list_before[2]),
                Rule(mask='9_neighbor.txt',lower_limit=rule_list_before[3],upper_limit=rule_list_before[4],result=rule_list_before[5]),
                Rule(mask='9_neighbor.txt',lower_limit=rule_list_before[6],upper_limit=rule_list_before[7],result=rule_list_before[8]),
                Rule(mask='9_neighbor.txt',lower_limit=rule_list_before[9],upper_limit=rule_list_before[10],result=rule_list_before[11]),
    
            ]



# Model with example ruleset
model = MncaModel(board_size=(500, 500),
                rules=rule_list, evolve_count = 50)

view = MncaView(model)
view.edit_traits(kind="livemodal")

print("reaching here")