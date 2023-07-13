# pyqt-prompt-listwidget
PyQt prompt generator widget for stable diffusion with 2 QListWidget

Required PyQt5.

Will be included in pyqt-stable-diffusion.

## Description
This app consists of Prompt 1 and Prompt 2.

Prompt 1 is a broad category that can be defined by factors such as hairstyle and the number of people.

Prompt 2 is a subcategory that can be defined by specific hairstyles (e.g., ponytail, straight).

Using this list, you can create your own prompts or generate prompts randomly.

The order of the categories and subcategories can be adjusted by drag and drop. Adjusting the order of the categories determines the priority of the prompts. Adjusting the order of the subcategories within a category affects the weighting when randomly selecting subattributes. The higher a subcategory is in the list, the higher its weight.

Only the checked items in the category list will be included in the random prompt generation. You can also choose whether to assign weights during random selection.

## Feature
- add & delete attributes(or properties if you will) for each prompt level
- support weight for randomizing
- support refresh button (which randomizes prompt again)

## Preview
![image](https://github.com/yjg30737/pyqt-prompt-listwidget/assets/55078043/2f2b492c-bcd6-401d-9e81-0283e0e5b5dd)
