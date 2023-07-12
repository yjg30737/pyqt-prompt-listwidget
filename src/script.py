import random

# things to add
# interaction
# male
# age


class PromptBuilder:
    PROMPT_DICT = {
        'number_of_people': ['1girl', '2girls', '3girls'],
        'hair_color': ['blonde hair', 'red hair', 'blue hair', 'dark hair'],
        'hair_style': ['long curly hair', 'long straight hair', 'short curly hair', 'short bob hair',
                       'short straight hair', 'ponytails hair'],
        'clothes': ['fancy top, miniskirt', 'white shirts, blue jeans', 'police uniform', 'cyberpunk clothes',
                    'sportswear', 'wearing glasses, tight top clothes'],
        'expression': ['grin', 'short smile', 'angry', 'laughing', 'screaming', 'sad', 'crying'],
        'pose': ['standing', 'sitting', 'kneeling', 'lying', 'leaning', 'cross-legged', 'crouching', 'squatting',
                 'bent', 'hunched', 'reclining', 'perched', 'balanced', 'folded', 'stretching', 'twisted', 'arched',
                 'curled', 'propped', 'resting', 'slouched', 'tilted', 'upright', 'tense', 'relaxed', 'inverted',
                 'raised', 'prone', 'supine', 'lunge', 'swaying', 'splayed', 'slumped', 'bowed', 'prostrate', 'poised',
                 'spread-eagle', 'curved', 'flexed', 'limber', 'balanced', 'folded', 'tangled', 'open', 'symmetrical',
                 'asymmetrical', 'tilting', 'rigidity', 'contrapposto', 'contorted'],
        'camera_distance': ['(extreme close-up:1.5)', '(medium full shot:1.5)', '(close-up:1.5)',
                            '(establishing shot:1.5)', '(medium close-up:1.5)', '(point-of-view:1.5)',
                            '(medium shot:1.5)', '(cowboy shot:1.5)', '(long shot:1.5)', '(upper body:1.5)',
                            '(full shot:1.5)', '(full body:1.5)'],
        'camera_angle': ['(front view:1.5)', '(from below:1.5)', '(bilaterally symmetrical:1.5)', '(from behind:1.5)',
                         '(side view:1.5)', '(wide angle view:1.5)', '(back view:1.5)', '(fisheyes view:1.5)',
                         '(from above:1.5)', '(macro view:1.5)', '(overhead shot:1.5)', '(straight on:1.5)',
                         '(top down view:1.5)', '(hero view:1.5)', "(bird's eye view:1.5)", '(low view:1.5)',
                         '(high angle:1.5)', "(worm's eye view:1.5)", '(slightly above:1.5)', '(selfie:1.5)'],
        'adding_lighting': ['bloom', 'backlight', 'sun light', 'soft lighting', 'god rays', 'studio light',
                            'hard lighting', 'volumetic lighting', 'bioluminescent light'],
        'wind': ['(wind:0)', '(wind:0.5)', '(wind:1)', '(wind:1.5)', '(wind:2)']
    }

    def __init__(self):
        super(PromptBuilder, self).__init__()
        self.__initVal()

    def __initVal(self):
        self.__current_prompt_dict = {}

    def generate_random_prompt(self, arr):
        if len(arr) > 0:
            max_len = max(map(lambda x: len(x), arr))
            weights = [i for i in range(max_len, 0, -1)]
            random_prompt = ', '.join(list(filter(lambda x: x != '', [random.choices(_, weights[:len(_)])[0] for _ in arr])))
        else:
            random_prompt = ''
        return random_prompt