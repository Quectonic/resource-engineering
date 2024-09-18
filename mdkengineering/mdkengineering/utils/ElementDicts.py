"""
    ****************************************************************************************
    
    1. ParagraphDict
        {
            "type": "paragraph",
            "level": <level int>,
            "content": [ ... TextDict, LinkDict, TextDict, ... ]
        }
        
    2. TextDict
        {
            "type": "text",
            "level": <level int>,
            "content": " ... Example Text ... "
        }
        
    3. LinkDict
        {
            "type": "link",
            "level" <level int>,
            "url": <link>,  
            "content": [ ... TextDict, FigureDict, TextDict ... ]
        }
        
    4. TableDict
        {
            "type": "table",
            "level": <level int>,
            "description": [ ... TextDict, LinkDict, ... ], 
            "row":  [ [ [ TextDict ], [ TextDict, LinkDict, ... ], ... ], 
                            [ [ TextDict ], [ TextDict, LinkDict, MediaDict ], ... ],
                            ...
                        ]
        }
        
    5. MediaDict
        {
            "type": "media",
            "level": <level int>,
            "description": [ ... TextDict, LinkDict, ... ], 
            "url": <url>, #### image source
        }
        
    6. HeadingDict
        {
            "type": "heading",
            "level": <level int>,
            "content": [ ... TextDict, LinkDict, TextDict ... ],
            "children": [ ... TextDict, ParagraphDict, TextDict ... ] 
        }
        
    7. ListDict
        {
            "type": "list",
            "level": <level int>,
            "item": [ ... [ ... TextDict ... ] ... ]
        }
        
    8. PlaceholderDict
        {
            "type": "placeholder",
            "level": <level int>,
            "content": ElementDict
        }
        
    ****************************************************************************************
"""

## Paragraph Test Example [PASS]
"""
    ParagraphDict = {
        "type": "paragraph",
        "level": 1,
        "content": [
            {
                "type": "text",
                "level": 2,
                "content": "This is an introductory paragraph discussing the "
            },
            {
                "type": "link",
                "level": 2,
                "url": "https://example.com",
                "content": [
                    {
                        "type": "text",
                        "level": 3,
                        "content": "importance of testing"
                    }
                ]
            },
            {
                "type": "text",
                "level": 2,
                "content": " in software development."
            }
        ]
    }
    - - - - - - - - - - - - - - - - - - 
    
    exampleText1 = TextDict(
        level=2,
        content="This is an introductory paragraph discussing the "
    )
    exampleText2 = TextDict(
        level=3,
        content="importance of testing"
    )
    exampleText3 = TextDict(
        level=2,
        content=" in software development."
    )
    exampleLink1 = LinkDict(
        level=2,
        content=[exampleText2]
    )
    examplePara1 = ParagraphDict(
        level=1,
        content=[
            exampleText1,
            exampleLink1,
            exampleText3
        ]
    )
"""

## Table Test Example
"""
    TableDict = {
        "type": "table",
        "level": 1,
        "description": [
            {
                "type": "text",
                "level": 2,
                "content": "Table 1 provides an overview of key metrics."
            }
        ],
        "row": [
            [
                [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "Metric"
                    }
                ],
                [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "Value"
                    }
                ]
            ],
            [
                [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "Accuracy"
                    }
                ],
                [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "95%"
                    }
                ]
            ],
            [
                [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "Precision"
                    }
                ],
                [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "approximately"    
                    },
                    {
                        "type": "link",
                        "level": 2,
                        "url": "https://example.com/precision",
                        "content": [
                            {
                                "type": "text",
                                "level": 3,
                                "content": "92%"
                            }
                        ]
                    }
                ]
            ]
        ]
    }
    
    - - - - - - - - - - - - - - - - - - 
    
    exampleDescriptionText1 = TextDict(level=2, content="Table 1 provides an overview of key metrics.")
    
    exampleText1 = TextDict(level=2, content="Metric")
    exampleText2 = TextDict(level=2, content="Value")
    exampleText3 = TextDict(level=2, content="Accuracy")
    exampleText4 = TextDict(level=2, content="95%")
    exampleText5 = TextDict(level=2, content="Precision")
    exampleText6 = TextDict(level=3, content="92%")
    exampleText7 = TextDict(level=2, content="approximately")
    exampleLink1 = LinkDict(level=2, url="https://example.com/precision", content=[exampleText6])
    
    exampleTable1 = TableDict(level=1, description=[exampleDescriptionText1], row=[[[exampleText1], [exampleText2]], [[exampleText3], [exampleText4]], [[exampleText5],[exampleText7, exampleLink1]]])
"""

## Media Test Example
"""
    MediaDict = {
        "type": "media",
        "level": 2,
        "description": [
            {
                "type": "text",
                "level": 2,
                "content": "An example image illustrating test coverage."
            }
        ],
        "source": "https://example.com/image.png"
    }
"""

## Advanced Test Examples
"""
    ComplexDict = {
        "type": "heading",
        "level": 1,
        "content": [
            {
                "type": "text",
                "level": 1,
                "content": "Overview"
            }
        ],
        "children": [
            {
                "type": "paragraph",
                "level": 2,
                "content": [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "This section covers the basics of "
                    },
                    {
                        "type": "link",
                        "level": 2,
                        "url": "https://example.com/basics",
                        "content": [
                            {
                                "type": "text",
                                "level": 2,
                                "content": "software testing"
                            }
                        ]
                    },
                    {
                        "type": "text",
                        "level": 2,
                        "content": " and its importance."
                    }
                ]
            },
            {
                "type": "media",
                "level": 2,
                "description": [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "Diagram of the testing process."
                    }
                ],
                "source": "https://example.com/testing-process.png"
            },
            {
                "type": "table",
                "level": 2,
                "description": [
                    {
                        "type": "text",
                        "level": 2,
                        "content": "Table showing test results."
                    }
                ],
                "content": [
                    [
                        [
                            {
                                "type": "text",
                                "level": 2,
                                "content": "Test Case"
                            }
                        ],
                        [
                            {
                                "type": "text",
                                "level": 2,
                                "content": "Result"
                            }
                        ]
                    ],
                    [
                        [
                            {
                                "type": "text",
                                "level": 2,
                                "content": "Login Test"
                            }
                        ],
                        [
                            {
                                "type": "text",
                                "level": 2,
                                "content": "Passed"
                            }
                        ]
                    ],
                    [
                        [
                            {
                                "type": "text",
                                "level": 2,
                                "content": "Signup Test"
                            }
                        ],
                        [
                            {
                                "type": "link",
                                "level": 2,
                                "url": "https://example.com/signup-test",
                                "content": [
                                    {
                                        "type": "text",
                                        "level": 2,
                                        "content": "Failed"
                                    }
                                ]
                            }
                        ]
                    ]
                ]
            }
        ]
    }
"""

## PROBLEM: 
## 1) design an instance creation pipeline such that there is no level input but 
##    instance can detect the level
##    1.1) yes/no: is a child content to be added to another non-header tag
##    1.2) yes/no: is a section content to be added to a header tag

import json
from abc import abstractmethod, ABC
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import re
from collections.abc import Iterable
from typing import Type, TypeVar, Generic
from mdkengineering.utils.DataTransformer import *

T = TypeVar('T', bound='ElementDict')

class MixinWithContentAttr(ABC, Generic[T]):
    
    """
    For ElementDict subclasses that contain 'content' as 
    a list attribute of class, acting as an inheritance template
    """
    
    def __init__(self, content: list[T] = []):
        self.content = content
    
    @abstractmethod
    def set_content(self, content: list[T] = []):
        self.content = content
        
    @abstractmethod
    def has_content(self):
        return self.getContentLength() != 0    
    
    @abstractmethod
    def getContentLength(self):
        return len(self.content)    
        
class MixinWithItemAttr(ABC, Generic[T]):
    
    """
    For ElementDict subclasses that contain 'item' as 
    a 2D (nested) list attribute of class, acting as an 
    inheritance template
    """
    
    def __init__(self, item: list[list[T]] = []):
        self.item = item
    
    @abstractmethod    
    def set_item(self, item: list[list[T]] = []):
        self.item = item
        
    @abstractmethod
    def has_item(self):
        return self.getItemLength() != 0
    
    @abstractmethod
    def getItemLength(self):
        return len(self.item)
        
class MixinWithRowAttr(ABC, Generic[T]):
    
    """
    For ElementDict subclasses that contain 'row' as 
    a 3D (nested) list attribute of class, acting as an 
    inheritance template
    """
    
    def __init__(self, row: list[list[list[T]]] = []):
        self.row = row
    
    @abstractmethod    
    def set_row(self, row: list[list[list[T]]] = []):
        self.row = row

    @classmethod
    def _to_dict_recursion(self, content):
        """Recursively process the content to handle nested structures."""
        if isinstance(content, list):
            return [self._to_dict_recursion(item) if isinstance(item, list) else item.to_dict() for item in content]
        return content
    
    @abstractmethod
    def has_row(self):
        for row_ in self.getTableDim():
            if (row_ != 0):
                return True
        return False
        
        
    @abstractmethod
    def getTableDim(self):
        for row_ in self.row:
            yield len(row_)
    
class MixinWithDescriptionAttr(ABC, Generic[T]):
    
    """
    For ElementDict subclasses that contain 'description' as 
    a list attribute of class, acting as an inheritance template
    """
    
    def __init__(self, description: list[T] = []):
        self.description = description
    
    @abstractmethod
    def set_description(self, description: list[T] = []):
        self.description = description
        
    @abstractmethod
    def has_description(self):
        return self.getDescriptionLength() != 0
    
    @abstractmethod
    def getDescriptionLength(self):
        return len(self.description)

class MixinWithChildrenAttr(ABC, Generic[T]):
    
    """
    For ElementDict subclasses that contain 'children' as 
    a list attribute of class, acting as an inheritance template
    """
    
    def __init__(self, children: list[T] = []):
        self.children = children
    
    @abstractmethod
    def set_children(self, children: list[T] = []):
        self.children = children
        
    @abstractmethod
    def has_children(self):
        return self.getChildrenLength() != 0
    
    @abstractmethod
    def getChildrenLength(self):
        return len(self.children)



## ElementDict Parent Class
class ElementDict(ABC):
    
    """
        Base class for all element dictionary classes
            - require level \<int\> and type \<str\> for parameters
    """
    
    allowed_types = [
        'paragraph',
        'link', 
        'media',
        'table',
        'text',
        'heading',
        'list',
        'placeholder'
    ]
    
    @classmethod
    def create_ElementDict(cls, level: int, type: str) -> 'ElementDict':
        """
        Factory method for creating ElementDict objects or its subclass objects
        """
        if type not in cls.allowed_types:
            raise TypeError('Type indicated was not allowed.')
        else:
            if type == 'paragraph':
                return ParagraphDict(level=level)
            elif type == 'link':
                return LinkDict(level=level)
            elif type == 'media':
                return MediaDict(level=level)
            elif type == 'text':
                return TextDict(level=level)
            elif type == 'table':
                return TableDict(level=level)
            elif type == 'heading':
                return HeadingDict(level=level)
            elif type == 'list':
                return ListDict(level=level)
            elif type == 'placeholder':
                return PlaceholderDict()
            
        
    
    def __init__(self, level: int, type: str) -> None:
        
        
        if type in ElementDict.allowed_types:
            self.type = type
        else:
            raise ValueError(f"Type of element cannot be {type}")
        
        if self.type == 'placeholder':
            self.level = None
        else:
            self.level = level

    @abstractmethod
    def to_dict(self) -> dict:
        """Convert class instance to dictionary."""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Stringify class content."""
        pass
    
    ## NOTE: Replaced by process_tag_to_class
    # @classmethod
    # @abstractmethod
    # def from_tag(cls, tag: BeautifulSoup) -> None:
    #     """Create instance from BeautifulSoup tag object."""
    #     pass
    
    @staticmethod
    def _to_dict_recursion(content):
        """Recursively process the content to handle nested structures."""
        if isinstance(content, list):
            return [ElementDict._to_dict_recursion(item) if isinstance(item, list) else item.to_dict() for item in content]
        return content
    
    @abstractmethod
    def set_level(self, level: int):
        self.level = level
    
    def incrementLevel(self, base_support_level):
        """Increment the level number based on parent ElementDict design."""
        self.level += base_support_level
        if hasattr(self, 'children') and self.children:
            for child in self.children:
                child.incrementLevel(self.level)
        if hasattr(self, 'description') and self.description:
            for descriptionChild in self.description:
                descriptionChild.incrementLevel(self.level)
        if hasattr(self, 'content') and self.content:
            for contentChild in self.content: 
                contentChild.incrementLevel(self.level)
    
    def prettify(self):
        
        """
        Turn content field of self class object and child class objects
        into one single string (article)
        
        Return(s)
        ----------
        - list[str]: nested list of contents
        - list[str] 1D list of contents
        - str: concatenated content
        """
        
        # content = self.extract_content()
        list_content = list(self.extract_content())
        flattened_content = list(ElementDict.flatten(self.extract_content()))
        parsed_result = ElementDict.content_stringify(flattened_content=flattened_content)
        
        return list_content, flattened_content, parsed_result
    
    @staticmethod
    def content_stringify(flattened_content):
        concatenated_content = ""
        table_parsing_mode = False
        for content in flattened_content:
            if (content == "<table>"):
                table_parsing_mode = not table_parsing_mode
                continue
            if (table_parsing_mode):
                table_transformer = HtmlTableTransformer(table_list=content)
                concatenated_content += table_transformer.toText()
                table_parsing_mode = not table_parsing_mode
            else:
                if isinstance(content, list):
                    concatenated_content += ElementDict.content_stringify(content)
                else:
                    concatenated_content += content
        return concatenated_content
    
    @staticmethod
    def flatten(nested_iterable) -> Iterable[str]:
        """
        Flatten nested list of strings using recursion
        
        Parameter(s)
        ----------
        nested_iterable: Iterable || Generator || list (nested list)
        
        Return(s)
        ----------
        Iterable[str]: 1D list of strings
        
        Note(s)
        ----------
        This function only flattens content that does not require
        formatting of any kind. 
        
        """
        
        item_list = list(nested_iterable)
        item_idx = 0
        while item_idx < len(item_list):
            if item_list[item_idx] == "<table>":
                yield "<table>"
                item_idx += 1
                yield item_list[item_idx]
            elif item_list[item_idx] == "<list>":
                yield "<list>"
                item_idx += 1
                yield item_list[item_idx]
            elif isinstance(item_list[item_idx], str):
                yield item_list[item_idx]
            elif isinstance(item_list[item_idx], Iterable) and not isinstance(item_list[item_idx], str):
                yield from ElementDict.flatten(item_list[item_idx])
            else:
                raise ValueError("Non-iterable and non-string item found in content")
            item_idx += 1
         
    def extract_content(self) -> Iterable[str]:
        """
        Recursively extracts values from ElementDict and convert them into
        textual formats.
        
        ***Note: this is not for parsing tag into ElementDict.***
    
        Parameter(s)
        ----------
        content: ElementDict \n
        The dictionary to extract content from
        
        Return(s)
        ----------
        []: A list of values found in 'content'
            - Only the textual content would be included 
            - Example: ["string from <p>", ]
        
        Note(s)
        ----------
        The returned list can either be a nested list or normal list
        """
                    
        def extract_table(rows):
            extracted_table = []
            for row in rows:
                extracted_row = []
                for cell in row:
                    extracted_cell = []
                    for content in cell:
                        extracted_cell = list(content.extract_content())
                    extracted_row.append(extracted_cell)
                extracted_table.append(extracted_row)
            return extracted_table
        
        def extract_list(rows):
            extracted_list = []
            for row in rows:
                extracted_row = []
                for content in row:
                    extracted_row = list(content.extract_content())
                extracted_list.append(extracted_row)
            return extracted_list
            
        if self.type == 'text':
            # Simply extract text
            yield self.content

        elif self.type == 'table':
            # Extract table content and description
            yield "\n\n"
            yield "<table>"
            
            # Extract table content
            if hasattr(self, 'content') and self.content and len(self.content) > 0:
                yield extract_table(self.content)  
            # Add description back if applicable
            if hasattr(self, 'description') and self.description:
                yield '\n'
                yield "Description of table: "
                for subdescription in self.description:
                    yield list(subdescription.extract_content())
            
            yield "\n\n"

        elif self.type == 'media':
            # Simply extract the link to the media and description
            yield f"{self.source}: "
            if hasattr(self, 'description') and self.description:
                for subdescription in self.description:
                    yield list(subdescription.extract_content())
                    

        elif self.type == 'heading':
            # Extract content and children, distinguishing section
            yield "\n\n\n"  # Start of the section
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    
            yield "\n\n"
            
            if hasattr(self, 'children') and self.children:
                for child in self.children:
                    yield list(child.extract_content())
                     
            yield "\n\n\n"  # End of the section

        elif self.type == 'link':
            # Extract nested items and attach reference URL
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    
                    
            if hasattr(self, 'url') and self.url:
                yield f"(refer to {self.url} for more explanation)"

        elif self.type == 'paragraph':
            # Extract nested items from the paragraph
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    
        elif self.type == 'list':
            ## Extract list item
            yield "<list>"
            if hasattr(self, 'item') and self.item and len(self.item) > 0:
                yield extract_list(self.content)
                
            pass
        
        elif self.type == 'placeholder':
            
            ## Extract nested content from the placeholder
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    
                
    @staticmethod    
    def from_bs_tag_with_hierarchy(tags: list[BeautifulSoup], base_level: int) -> 'ElementDict':
        """
        Recursively process tags and sub-tags and return an ElementDict
        with hierarchical content, description, etc. 
        
        Parameter(s)
        ----------
        tag: list[BeautifulSoup]
             -  should be a list of tags
        
        Return(s)
        ----------
        list[ElementDict] 
             -  each with nested structure
        
        Example(s)
        ----------
        Given an example html:

            <h1>Hello World</h1>
            <p>This is a <a href="example url">Hello World</a> program.</p>
            <p>It is super fun.</p>
            <h2>Origin of <a href="example url 2">Programming</a></h2>
            <p>You might have to contact <a href="example url 3">Alan Turing</a> to understand:</p>
            <ul>
                <li>How programming started.</li>
                <li>Why it is important.</li>
            </ul>
            <h1>Decipher</h1>
            <p>This is related to <a href="example url 4">cryptography</a>, which I have no idea about.</p>
            
           
        Return:
        
            [
                HeadingDict(
                    level=1,
                    content=[
                        TextDict(
                            level=2,
                            content="Hello World"    
                        )
                    ],
                    children=[
                        ParagraphDict(
                            level=2, 
                            content=[
                                TextDict(
                                    level=3, 
                                    content="This is a "
                                ),
                                LinkDict(
                                    level=3,
                                    url="example url",
                                    content=[
                                        TextDict(
                                            level=4,
                                            content="Hello World"
                                        )
                                    ]
                                ),
                                TextDict(
                                    level=3,
                                    content=" program."
                                )
                            ]
                        ),
                        ParagraphDict(
                            level=2,
                            content=[
                                TextDict(
                                    level=3,
                                    content="It is super fun."
                                )
                            ]
                        ),
                        HeadingDict(
                            level=2,
                            content=[
                                TextDict(
                                    level=3, 
                                    content="Origin of "
                                ),
                                LinkDict(
                                    level=3,
                                    url="example url 2"
                                    content=[
                                        TextDict(
                                            level=4,
                                            content="Programming"
                                        )
                                    ]
                                )
                            ],
                            children=[
                                ParagraphDict(
                                    level=3,
                                    content=[
                                        TextDict(
                                            level=4,
                                            content="You might have to contact "
                                        ),
                                        LinkDict(
                                            level=4,
                                            url="example url 3",
                                            content=[
                                                TextDict(
                                                    level=5,
                                                    content="Alan Turing"
                                                )
                                            ]
                                        ),
                                        TextDict(
                                            level=4,
                                            content=" to understand:"
                                        )
                                    ]
                                ),
                                ListDict(
                                    level=3,
                                    item=[
                                        [
                                            TextDict(
                                                level=4,
                                                content="How programming started."
                                            )
                                        ],
                                        [
                                            TextDict(
                                                level=4,
                                                content="Why it is important."
                                            )
                                        ]
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                HeadingDict(
                    level=1,
                    content=[
                        TextDict(
                            level=2,
                            content="Decipher"
                        )
                    ],
                    children=[
                        TextDict(
                            level=2,
                            content="This is related to "
                        ),
                        LinkDict(
                            level=2,
                            url="example url 4",
                            content=[
                                TextDict(
                                    level=3,
                                    content="cryptography"
                                )
                            ]
                        ),
                        TextDict(
                            level=2,
                            content=", which I have no idea about."
                        )
                    ]
                )
            ]
        """
        
        ## Receive a list of bs4 object(s)
        ## return a list of ElementDict(s)
        
        
        ## TODO
        
        if not tags and any(not isinstance(item, BeautifulSoup) for item in tags):
            raise ValueError(f'{ElementDict.from_bs_tag.__name__} did not receive a valid BeautifulSoup tag for processing')
        
        ## base case: subtags[idx] does not have a tag name and contains only text
        ## recursion case: subtags[idx] has a tag name
        
        ## QUESTION
        ##       -  Upon reaching heading tag, update the level value
        ##           -  With the new level value, how do program switch to a different branch?
        ##           -  Use the level value to find the closest sibling heading tag with the same level
        ##                                                                              |--> h1 => level 1
        ##                                                                                      |--> content level 1 + 1
        
        nested_content_list = list()
        idx = 0
        current_level = base_level
        last_header_position, last_header_level = -1, -1 ## record the index of the heading tag in the 
        while idx < len(tags):
            current_tag = tags[idx]
            
            if re.match(r'h\d+', current_tag.name) and type(current_tag) is Tag:
                current_level = int(current_tag.name[1:])
                ## LOGIC TO COMPARE TO LAST HEADING TAG ETC.
                
                if last_header_position == -1:
                    
                    ## no prior heading tag found 
                    support_structure = HeadingDict(
                        level=current_level,
                        content=[],
                        children=[],
                    )
                    for tmp_support_level in range(current_level-1, 0, -1):
                        ## assuming heading tags are outermost
                        if support_structure is None:
                            support_structure = PlaceholderDict(
                                level=tmp_support_level,
                                
                            )
                
                
                
                
                last_header_position, last_header_level = idx, current_level
                    
                    
        ## Step 1:
        ##       -  turn every tag in tags.contents to be ElementDict
        
        
        def parse_nested_tags(tags: list[BeautifulSoup]):
            for tag in tags:
                pass
                
        
        ## Step 2:
        ##       -  sorting ElementDicts into hierarchy
        
        ## Step 3:
        ##       -  standalone, unsupported heading tag get PlaceholderDict
        
        
        ## Step 4:
        ##       -  clean the empty content ElementDicts
        ##           1. nested with other ElementDict but consist of no valuable content
        ##           2. nested alone under header or paragraph and consist of no valuable content
        
        
        # ***************************************************************************************************
        # ***************************************************************************************************
        # ***********   Content Cases:                                                            ***********
        # ***********    -  tag has content --> recursion over the tag parameter                  ***********
        # ***********                       --> assign list of ElementDict to the parent          ***********
        # ***********                           tag through recursion                             ***********
        # ***********    -  tag has children --> while loop                                       ***********
        # ***********                        --> go through subsequent tags until reaching        ***********
        # ***********                            the next heading tag                             ***********
        # ***********                            |--> once reaching the next heading tag,         ***********
        # ***********                                 compare hierarchical indicator (h<int>)     ***********
        # ***********                                 of the next tag to the current tag of       ***********
        # ***********                                 the loop                                    ***********
        # ***********                                 |--> bigger  ==> go into children           ***********
        # ***********                                 |--> equal   ==> append new item to         ***********
        # ***********                                                  the existing list          ***********
        # ***********                                 |--> smaller ==> ????                       ***********    
        # ***********                                                                             ***********
        # ***********   Type Cases:                                                               ***********
        # ***********    -  <Figure>, <Gallery> --> Media                                         ***********
        # ***********    -  <a> --> link                                                          ***********
        # ***********    -  <p> --> paragraph                                                     ***********
        # ***********    -  <h(\d+)> --> heading                                                  ***********
        # ***********    -  <div>, <section>, <body> --> placeholder                              ***********
        # ***********    -  <ul> --> list                                                         ***********
        # ***********    -  no tag --> text                                                       ***********
        # ***********    -  <table> --> table                                                     ***********
        # ***************************************************************************************************
        # ***************************************************************************************************
        
        
    
    

class ParagraphDict(ElementDict, MixinWithContentAttr[T]):
    
    def __init__(self,  level: int = None, content: list[T] = []) -> None:
        super().__init__(level=level, type='paragraph')
        ## NOTE
        # self.content = content
        MixinWithContentAttr.__init__(self, content=content)
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "content": [item.to_dict() for item in self.content if item is not None]
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_content(self, content: list[T] = []):
        return super().set_content(content)
    
    def set_level(self, level: int):
        return super().set_level(level)
    
    def getContentLength(self):
        return super().getContentLength()
    
    def has_content(self):
        return super().has_content()
    
    
class LinkDict(ElementDict, MixinWithContentAttr[T]):
    def __init__(self, level: int = None, url: str = "", content: list[T] = []) -> None:
        super().__init__(level=level, type='link')
        MixinWithContentAttr.__init__(self, content=content)
        self.url = url
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "url": self.url,
                "content": [item.to_dict() for item in self.content if item is not None]
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_content(self, content: list[T] = []):
        return super().set_content(content)
    
    def set_level(self, level: int):
        return super().set_level(level)
    
    def getContentLength(self):
        return super().getContentLength()
    
    def has_content(self):
        return super().has_content()
    
        
class TextDict(ElementDict):
    def __init__(self, level: int = None, content: str = "", italic: bool = False, bold: bool = False) -> None:
        super().__init__(level=level, type='text')
        self.content = content
        self.annotation = {
            'bold': bold,
            'italic': italic
        }
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "content": self.content,
                "annotation": self.annotation
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_content(self, content: str = ""):
        self.content = content
        
    def set_level(self, level: int):
        return super().set_level(level)
    
    
class MediaDict(ElementDict, MixinWithDescriptionAttr[T]):
    def __init__(self,  level: int = None, description: list[T] = [], url: str = "") -> None:
        super().__init__(level=level, type='media')
        MixinWithDescriptionAttr.__init__(self, description=description)
        self.url = url
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "description": [item.to_dict() for item in self.description if item is not None],
                "url": self.url
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_description(self, description: list[T] = []):
        return super().set_description(description)
    
    def set_level(self, level: int):
        return super().set_level(level)
    
    def has_description(self):
        return super().has_description()
    
    def getDescriptionLength(self):
        return super().getDescriptionLength()
    
    
    
class TableDict(ElementDict, MixinWithDescriptionAttr[T], MixinWithRowAttr[T]):
    def __init__(self,  level: int = None, description: list[T] = [], row: list[list[list[T]]] = []) -> None:
        super().__init__(level=level, type='table')
        MixinWithRowAttr.__init__(self, row=row)
        MixinWithDescriptionAttr.__init__(self, description=description)
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "description": [item.to_dict() for item in self.description if item is not None],
                "row": ElementDict._to_dict_recursion(self.row) 
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_description(self, description: list = []):
        return super().set_description(description)
    
    def set_row(self, row: list[list[list[T]]] = []):
        return super().set_row(row)
    
    def set_level(self, level: int):
        return super().set_level(level)
    
    def _to_dict_recursion(self, content):
        """Recursively process the content to handle nested structures."""
        if isinstance(content, list):
            return [self._to_dict_recursion(item) if isinstance(item, list) else item.to_dict() for item in content]
        return content
    
    def has_description(self):
        return super().has_description()
    
    def getDescriptionLength(self):
        return super().getDescriptionLength()
    
    def has_row(self):
        return super().has_row()
    
    def getTableDim(self):
        return super().getTableDim()
    
    
    
    
class HeadingDict(ElementDict, MixinWithChildrenAttr, MixinWithContentAttr):
    
    """
    Note(s)
    --------------
     -  Inner headings only exists if outer heading exists
         -  h2 exists only if h1 exists
     
     
    """
    
    def __init__(self,  level: int = None, children: list[T] = [], content: list[T] = []) -> None:
        super().__init__(level=level, type='heading')
        MixinWithChildrenAttr.__init__(self, children=children)
        MixinWithContentAttr.__init__(self, content=content)
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "children": [item.to_dict() for item in self.children if item is not None],
                "content": [item.to_dict() for item in self.content if item is not None]
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_children(self, children: list = []):
        return super().set_children(children)
    
    def set_content(self, content: list = []):
        return super().set_content(content)
    
    def set_level(self, level: int):
        return super().set_level(level)
    
    def getChildrenLength(self):
        return super().getChildrenLength()
    
    def getContentLength(self):
        return super().getContentLength()
    
    def has_children(self):
        return super().has_children()
    
    def has_content(self):
        return super().has_content()
    
    
class ListDict(ElementDict, MixinWithItemAttr[T]):
    
    def __init__(self, level: int = None, item: list[list[T]] = []) -> None:
        super().__init__(level=level, type='list')
        MixinWithItemAttr.__init__(self, item=item)
        
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "level": self.level,
            "item": ElementDict._to_dict_recursion(self.item) 
        }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
        
    def set_item(self, item: list[list[T]] = []):
        return super().set_item(item)
    
    def set_level(self, level: int):
        return super().set_level(level)
    
    def _to_dict_recursion(self, content):
        """Recursively process the content to handle nested structures."""
        if isinstance(content, list):
            return [self._to_dict_recursion(item) if isinstance(item, list) else item.to_dict() for item in content]
        return content

    def has_item(self):
        return super().has_item()
    
    def getItemLength(self):
        return super().getItemLength()


class PlaceholderDict(ElementDict, MixinWithContentAttr[T]):
    
    """
    Use cases
    ---------
     -  div, body, section, etc.
    """
    
    def __init__(self, content: list[T] = []) -> None:
        super().__init__(level=None, type='placeholder')
        MixinWithContentAttr.__init__(self, content=content)
        
    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "content": [item.to_dict() for item in self.content if item is not None],
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    def set_content(self, content: list[T] = []):
        return super().set_content(content)
    
    def set_level(self, level: int):
        raise TypeError(f'{PlaceholderDict.__name__} class does not support leveling. {PlaceholderDict.set_level.__name__} not implemented.')
    
    def has_content(self):
        return super().has_content()
    
    def getContentLength(self):
        return super().getContentLength