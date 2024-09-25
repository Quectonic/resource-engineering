from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from typing import TypeVar
from mdkengineering.utils.ElementDicts import *
from mdkengineering.utils.DataTransformer import *
import textwrap

T = TypeVar('T', bound=ElementDict) 

def transform_tag_to_ElementDict(tag: Tag | NavigableString, base_url: str = "",
                                    verbose: bool = False, indent: int = 0, 
                                    # current_location: list[int] = None,
                                    # origin: bool = True,
                                ) -> list[T] | T:
    
    """
    Parse single BeautifulSoup tag into ElementDict
    
    Parameter(s)
    ------------
    tag: BeautifulSoup
    base_url: str --> the base url of the website [optional]
    verbose: bool --> whether or not to print the parsing process [optional]
    indent: int --> the indentation level of the print [optional]
    current_location: list[int] --> the current location of the tag in the list [optional]
    origin: bool --> whether or not the tag is the outermost tag [optional]
    
    
    Return(s)
    ------------
    list[ElementDict]
     -  the returned list is a placeholder if the Tag is the outermost encapsulating
        div tag
    
    Note(s)
    ------------
    For the following tags, the content would be parsed as well:
        -  \<p\>
        -  \<a\>
        
        
    Use Case(s)
    -----------
    .. code-block:: python
        return [transform_tag_to_ElementDict(subtag, ...) for subtag in surroundingTag]
    """
    
    
    if type(tag) is NavigableString:
        ## print(f'text detected')
        
        return TextDict(
            content=tag, 
            # indices=current_location,
        )
    
    elif tag.name and re.match(r'h\d+', tag.name):
        ## print(f'heading detected')
        
        tmp_level = int(tag.name[1:])
        heading_content = list()
        for idx, item in enumerate(tag.contents):
            # if current_location is not None and isinstance(current_location, list):
#                location = current_location.append(idx)
#            else:
#                location = None
            parsed_item = transform_tag_to_ElementDict(
                item, verbose=verbose, indent=indent+4, 
                # current_location=location, origin=False
                )
            if verbose:
                indented_message = textwrap.indent(f"Appending from heading condition: {parsed_item}", f"{' ' * indent}")
                print(indented_message)
            heading_content.append(parsed_item)
        
        
        heading = HeadingDict(
            level=tmp_level, content=heading_content, 
            # indices=current_location,
            )
        
        # print(f'heading_content: {heading_content}')
        return heading
    
    elif tag.name == 'b':
        if verbose:
            indented_message = textwrap.indent(f"Appending from bold text: {tag.get_text()}", f"{' ' * indent}")
            print(indented_message)
        return TextDict(
            content=tag.get_text(), bold=True, 
            # indices=current_location,
            )
    
    elif tag.name == 'i':
        if verbose:
            indented_message = textwrap.indent(f"Appending from italic text: {tag.get_text()}", f"{' ' * indent}")
            print(indented_message)
        return TextDict(
            content=tag.get_text(), italic=True, 
            # indices=current_location,
            )
    
    elif tag.name == 'p':
        ## print(f'paragraph detected')
        
        paragraph_content = list()
        for idx, item in enumerate(tag.contents):
            # if current_location is not None and isinstance(current_location, list):
#                location = current_location.append(idx)
#            else:
#                location = None
            parsed_item = transform_tag_to_ElementDict(item, verbose=verbose, indent=indent+4, 
                                                    #    current_location=location, origin=False
                                                       )
            if verbose:
                indented_message = textwrap.indent(f"Appending from paragraph condition: {parsed_item}", f"{' ' * indent}")
                print(indented_message)
            paragraph_content.append(parsed_item)
            
            
        return ParagraphDict(
            content=paragraph_content,
            # indices=current_location,
        )
        
    elif tag.name == 'a':
        ## print(f'link detected')
        
        link_content = list()
        
        for idx, item in enumerate(tag.contents):
            # if current_location is not None and isinstance(current_location, list):
#                location = current_location.append(idx)
#            else:
#                location = None
            parsed_item = transform_tag_to_ElementDict(item, verbose=verbose, indent=indent+4,
                                                    #    current_location=location, origin=False
                                                       )
            if verbose:
                indented_message = textwrap.indent(f"Appending from link condition: {parsed_item}", f"{' ' * indent}")
                print(indented_message)
            link_content.append(parsed_item)
            
        return LinkDict(
            url=str(tag.get("href")),
            content=link_content,
            # indices=current_location,
        )
        
    elif tag.name == 'table':
        ## print(f'table detected')
        
        ## Table
        
        tableTransformer = HtmlTableTransformer(table_html=str(tag))
        caption = list()
        if tag.find('caption'):
            for caption_item in tag.find('caption').contents:
                parsed_item = transform_tag_to_ElementDict(caption_item, verbose=verbose, indent=indent+4, 
                                                        #    origin=False
                                                           )
                if verbose:
                    indented_message = textwrap.indent(f"Appending from table caption condition: {parsed_item}", f"{' ' * indent}")
                    print(indented_message)
                caption.append(parsed_item)
            
        return TableDict(
            description=caption,
            row=tableTransformer.table_ED_list
        )
    
    elif tag.name == 'ul':
        ## print(f'list detected')
        
        ## List
        
        items = list()
        
        for list_bulletin in tag.find_all('li'):
            sub_content = list()
            for list_item in list_bulletin.contents:
                parsed_item = transform_tag_to_ElementDict(list_item, verbose=verbose, indent=indent+4, 
                                                        #    origin=False
                                                           )
                if verbose:
                    indented_message = textwrap.indent(f"Appending from list condition: {parsed_item}", f"{' ' * indent}")
                    print(indented_message)
                sub_content.append(parsed_item)
            items.append(sub_content)
        return ListDict(
            item=items
        )
    
    elif tag.name == 'figure':
        ## print(f'figure detected')
        
        ## Media
        
        caption_contents = tag.find('figcaption').contents
        caption = list()
        for idx, caption_item in enumerate(caption_contents):
            # if current_location is not None and isinstance(current_location, list):
#                location = current_location.append(idx)
#            else:
#                location = None
            parsed_item = transform_tag_to_ElementDict(caption_item, verbose=verbose, indent=indent+4, 
                                                    #    current_location=location, origin=False
                                                       )
            if verbose:
                indented_message = textwrap.indent(f"Appending from figure caption content (can be any ElementDict type) condition: {parsed_item}", f"{' ' * indent}")
                print(indented_message)
            caption.append(parsed_item)
        
        source = tag.find('img').attrs['src']
        
        return MediaDict(
            description=caption,
            url=base_url+source,
            # indices=current_location,
        )
        
    
    elif tag.name == 'li' and 'gallerybox' in tag.get('class', []):
        ## print(f'li detected')
        
        ## Media
        
        caption_contents = tag.find('div', attrs={"class": "gallerytext"}).contents
        caption = list()
        for idx, caption_item in enumerate(caption_contents):
            # if current_location is not None and isinstance(current_location, list):
#                location = current_location.append(idx)
#            else:
#                location = None
            parsed_item = transform_tag_to_ElementDict(caption_item, verbose=verbose, indent=indent+4,
                                                    #    current_location=location, origin=False
                                                       )
            if verbose:
                indented_message = textwrap.indent(f"Appending from gallerybox caption content (can be any ElementDict type) condition: {parsed_item}", f"{' ' * indent}")
                print(indented_message)
            caption.append(parsed_item)
        
        source = tag.find('img').attrs['src']
        
        return MediaDict(
            description=caption,
            url=base_url+source,
            # indices=current_location,
        )
        
    # elif tag.name == 'div' or tag.name == 'section' or tag.name == 'body':
    else:
        ## print(f'{tag.name} detected')
        content = list()
        
        for idx, subtag in enumerate(tag.contents):
            # if current_location is not None and isinstance(current_location, list):
#                location = current_location.append(idx)
#            else:
#                location = None
            content.append(transform_tag_to_ElementDict(subtag, verbose=verbose, indent=indent+4, 
                                                        # current_location=location, origin=False
                                                        )
                           )
        
        return PlaceholderDict(
            content=content,
            # indices=current_location,
        )
        # return [transform_tag_to_ElementDict(subtag) for subtag in tag.contents]
    
    
def add_header_enclosure(children_elements: list[ElementDict] = [], content_elements: list[ElementDict] = [], indices: list[int] = []):
    
    """
    Adding a heading ElementDict to encapsulate the list of elements
    """
    
    ## TODO: get the outermost 
    
    level = 1
    for idx, element in enumerate(children_elements):
        if type(element) == HeadingDict:
            level = element.level - 1
    
    if level <= 0:
        level = 1
    
    return HeadingDict(
        level=1,
        children=children_elements,
        content=content_elements,
        indices=indices
    )
        
        
def find_inner_elements(content, path=None, element_type=HeadingDict, cut_off=True):
    """
    Description(s)
    --------------
    This is a function that checks for the existence of inner HeadingDict 
    or other ElementDict type if specified. 

    **Best to be used on the outermost ElementDict layer of any object**
        --> the previous content indices are not recorded, so use it for inner layers 
            only if the indices is well known
    
    
    Parameter(s)
    ------------
    content: ElementDict[] --> EXCEPT HeadingDict
    path: int[] --> Recursive parameter to indicate previous path visited
    element_type: ElementDict --> the type to be found inside the nested ElementDicts
    cut_off: boolean --> whether or not the finding algorithm should stop upon reaching a target element

    Return(s)
    ---------
    int[] --> indices of the nested HeadingDict
            --> if empty, then empty list is returned
            --> e.g. [0, 1, 2] --> target HeadingDict is            \
                                    the THIRD (idx=2) element of    \
                                    the SECOND (idx=1) element of   \
                                    the FIRST (idx=0) element of    \
                                    the content list
    """  
    if path is None:
        path = []

    headings = []

    for i, item in enumerate(content):
        current_path = path + [i]
        
        if item and isinstance(item, element_type) and current_path:
            ## Base Case
            
            headings.append(current_path)
            if cut_off:
                continue

        if hasattr(item, 'content') and isinstance(item.content, list):
            headings.extend(find_inner_elements(item.content, path=current_path, element_type=element_type))

    return headings


        
def sort_element_order(elements: list[ElementDict] = []):
    
    """
    Rearrange elements into nested ElementDict structure
    
    
    Assumption(s)
    -------------
     1. All headers are not surrounded by content sectioning elements\n
        e.g. span, div, nav, footer, articles, etc.  
        
        
    Use case(s)
    -------------
    .. code-block:: python
        for subtag in 
    """
    
    if len(elements) == 0:
        raise ValueError('No value is found inside elements. An empty list received.')
    
    ## step 1:  put non heading ElementDicts into children of last HeadingDict 
    ##           -  in this case the resulting list should:
    ##               1. only consist of HeadingDict(s)
    
    
    ## PROBLEM: 
    ##           - What if we have the following:
    ##              <h1>heading 1</h1>
    ##              <div><h1>heading 2</h1></div>
    
    heading_only_elements = list()
    
    for idx, item in enumerate(elements):
        if item and isinstance(item, HeadingDict):
            heading_only_elements.append(item)
        else:
            
            ## TODO:    set the level of the nested ElementDict before appending
            ##           -  new function might be needed
            try: 
                heading_only_elements[-1].content.append(item)            
            except Exception as error:
                print(f'Appending failed: {error}')
    
    ## step 2:  compare and nest heading ElementDicts into one another if necessary
    ##           -  Consist of headings only
    ##           -  nested concept for list
    
    ## PROBLEM: 
    ##           - What if we have the following:
    ##              <h1>heading 1</h1>
    ##              <div><h1>heading 2</h1></div>
    ordered_elements = list()
    curr_level = 0
    
    for idx, item in enumerate(heading_only_elements):
        if len(ordered_elements) == 0:
            ordered_elements.append(item)
            continue
        
        
        if item and hasattr(ordered_elements, 'level'):
            if item.level == ordered_elements[-1].level:
                ordered_elements.append(item)
            
    ## step 3: 