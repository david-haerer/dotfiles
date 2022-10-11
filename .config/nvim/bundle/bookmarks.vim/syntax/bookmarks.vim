" A URL is one line that starts with 'http[s]://'.
syntax  match  URL       '^https*:\/\/.*$'

" A name must be at the beginning of the file or after a newline,
" it can have any character and must be followed by a line with a URL.
syntax  match  Name      '\(^\n\|\%^\)\@<=.*\(\nhttps*:\/\/\)\@='

" A list of tags must be at the end of the file or followed by a newline,
" it can have any character and must be after a line with a URL.
" syntax match Tags '\(^https*:\/\/.*\n\)\@<=.*\(\n\n\|\%$\)\@='
syntax  match  Tags      '\(^https*:\/\/.*\n\)\@<=.\+\(\n\n\|\%$\)\@='  contains=Star,Type,Language

" A star is the tag '*'.
syntax  match  Star      '\(^\|\s\)\@<=\*\($\|\s\)\@='                  contained

" A type is a tag that starts with a colon.
syntax  match  Type      '\(^\|\s\)\@<=:[^[:blank:]]\+\($\|\s\)\@='     contained

" A language is one of the tags 'EN', 'DE' or 'FR'.
syntax  match  Language  '\(^\|\s\)\@<=EN\|DE\|FR\($\|\s\)\@='          contained

highlight default link Name String
highlight default link URL Constant
highlight default link Tags Keyword
highlight default link Star Statement
highlight default link Type Type
highlight default link Language Delimiter
