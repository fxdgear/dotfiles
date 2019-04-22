func! myspacevim#before() abort
  let g:vimfiler_direction = 'topleft'
  let g:tagbar_vertical = 10
  let g:tagbar_left = 1
  autocmd BufWritePre * %s/\s\+$//e
  autocmd BufWritePre *.py execute ':Black'
  let g:vimfiler_ignore_pattern =
        \ '^\%(\.git\|\.idea\|\.DS_Store\|\.vagrant\|.stversions'
        \ .'\|node_modules\|.*\.pyc\)$'
endf
