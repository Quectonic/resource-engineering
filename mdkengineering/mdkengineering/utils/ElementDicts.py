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
            "content":  [ [ [ TextDict ], [ TextDict, LinkDict, ... ], ... ], 
                            [ [ TextDict ], [ TextDict, LinkDict, MediaDict ], ... ],
                            ...
                        ]
        }
        
    5. MediaDict
        {
            "type": "media",
            "level": <level int>,
            "description": [ ... TextDict, LinkDict, ... ], 
            "source": <url>, #### image source
        }
        
    6. HeadingDict
        {
            "type": "heading",
            "level": <level int>,
            "content": [ ... TextDict, LinkDict, TextDict ... ],
            "children": [ ... TextDict, ParagraphDict, TextDict ... ] 
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
        "content": [
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
    
    exampleTable1 = TableDict(level=1, description=[exampleDescriptionText1], content=[[[exampleText1], [exampleText2]], [[exampleText3], [exampleText4]], [[exampleText5],[exampleText7, exampleLink1]]])
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
from collections.abc import Iterable

class ElementDict(ABC):
    
    """
        Base class for all element dictionary classes
            - require level \<int\> and type \<str\> for parameters
    """
    
    def __init__(self, level: int, type: str) -> None:
        self.level = level
        if type in self.allowed_types:
            self.type = type
        else:
            raise ValueError(f"Type of element cannot be {type}")
    
    @property
    def allowed_types(self):
        return [
            'paragraph',
            'link', 
            'media',
            'table',
            'text',
            'heading'
        ]

    @abstractmethod
    def to_dict(self) -> dict:
        """Convert class instance to dictionary."""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Stringify class content."""
        pass
    
    @classmethod
    @abstractmethod
    def from_tag(cls, tag: BeautifulSoup) -> None:
        """Create instance from BeautifulSoup tag object."""
        pass
    
    @classmethod
    @abstractmethod
    def from_string_tag(cls, tag: str) -> None:
        """Create instance from stringified BeautifulSoup tag."""
        pass
    
    def prettify(self):
        # content = self.extract_content()
        listed_content = list(self.extract_content())
        flattened_content = list(self.flatten(self.extract_content()))
        return listed_content, flattened_content, "".join(flattened_content)
    
    def flatten(self, nested_iterable) -> Iterable[str]:
        # print(f'nested_iterable: {next(nested_iterable)}')
        for item in nested_iterable:
            if isinstance(item, str):
                yield item
            elif isinstance(item, Iterable) and not isinstance(item, str):
                print(f'flattening: {item}')
                yield from self.flatten(item)  # Recursive call to flatten the sub-iterable
            else:
                raise ValueError("Non-iterable and non-string item found in content")
    
    def extract_content(self) -> Iterable[str]:
        """
        Recursively extracts values from ElementDict.
    
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
        
        ## TODO
        def extract_content_in_list(listofcontent):
            for subcontent in listofcontent:
                pass
            
        if self.type == 'text':
            # Simply extract text
            yield self.content

        elif self.type == 'table':
            # Extract table content and description
            yield "\n"
            
            # Extract table content
            if self.content and len(self.content) > 0:
                for subcontent in self.content:
                    """
                        ## TODO
                        - subcontent can be a list
                        - need to filter 
                    """
                    if isinstance(subcontent, list):
                        pass
                    else:
                        yield list(subcontent.extract_content())
                        # yield from subcontent.extract_content()
            
            # Add description back if applicable
            if hasattr(self, 'description') and self.description:
                yield "Description of table: "
                for subdescription in self.description:
                    yield list(subdescription.extract_content())
                    # yield from subdescription.extract_content()
            
            yield "\n"

        elif self.type == 'media':
            # Simply extract the link to the media and description
            yield f"{self.source}: "
            if hasattr(self, 'description') and self.description:
                for subdescription in self.description:
                    yield list(subdescription.extract_content())
                    # yield from subdescription.extract_content()

        elif self.type == 'heading':
            # Extract content and children, distinguishing section
            yield "\n\n\n"  # Start of the section
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    # yield from subcontent.extract_content()
            
            if hasattr(self, 'children') and self.children:
                for child in self.children:
                    yield list(child.extract_content())
                    # yield from child.extract_content() 
            yield "\n\n\n"  # End of the section

        elif self.type == 'link':
            # Extract nested items and attach reference URL
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    # yield from subcontent.extract_content()
                    
            if hasattr(self, 'url') and self.url:
                yield f"(refer to {self.url} for more explanation)"

        elif self.type == 'paragraph':
            # Extract nested items from the paragraph
            if hasattr(self, 'content') and self.content:
                for subcontent in self.content:
                    yield list(subcontent.extract_content())
                    # yield from subcontent.extract_content()
    

class ParagraphDict(ElementDict):
    def __init__(self,  level: int, content: list[ElementDict] = []) -> None:
        super().__init__(level=level, type='paragraph')
        self.content = content
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "content": self.content
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
    @classmethod
    def from_tag(cls, tag: BeautifulSoup) -> None:
        return super().from_tag(tag)
    
class LinkDict(ElementDict):
    def __init__(self, level: int, url: str = "", content: list[ElementDict] = []) -> None:
        super().__init__(level=level, type='link')
        self.url = url
        self.content = content
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "content": self.content
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
        
class TextDict(ElementDict):
    def __init__(self, level: int, content: str = "") -> None:
        super().__init__(level=level, type='text')
        self.content = content
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "content": self.content
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
class MediaDict(ElementDict):
    def __init__(self,  level: int, description: list[ElementDict] = [], url: str = "") -> None:
        super().__init__(level=level, type='media')
        self.description = description
        self.url = url
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "description": self.description,
                "url": self.url
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
class TableDict(ElementDict):
    def __init__(self,  level: int, description: list[ElementDict] = [], content: list[ElementDict] = []) -> None:
        super().__init__(level=level, type='table')
        self.description = description
        self.content = content
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "description": self.description,
                "content": self.content
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
    
class HeadingDict(ElementDict):
    def __init__(self,  level: int, children: list[ElementDict] = [], content: list[ElementDict] = []) -> None:
        super().__init__(level=level, type='heading')
        self.children = children
        self.content = content
        
    def to_dict(self) -> dict:
        return {
                "type": self.type,
                "level": self.level,
                "description": self.description,
                "url": self.url
            }
        
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)