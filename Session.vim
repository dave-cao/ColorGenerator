let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/Coding_Projects/Currently_Working/ColorGenerator
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +10 main.py
badd +13 templates/base.html
badd +2 templates/index.html
badd +0 image_handle.py
argglobal
%argdel
$argadd main.py
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit main.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 92 + 94) / 189)
exe 'vert 2resize ' . ((&columns * 96 + 94) / 189)
tcd ~/Documents/Coding_Projects/Currently_Working/ColorGenerator
argglobal
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
23
normal! zo
24
normal! zo
28
normal! zo
33
normal! zo
39
normal! zo
42
normal! zo
let s:l = 23 - ((10 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 23
normal! 032|
wincmd w
argglobal
if bufexists(fnamemodify("~/Documents/Coding_Projects/Currently_Working/ColorGenerator/templates/index.html", ":p")) | buffer ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/templates/index.html | else | edit ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/templates/index.html | endif
balt ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/main.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
5
normal! zo
7
normal! zo
13
normal! zo
let s:l = 7 - ((6 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 7
normal! 015|
wincmd w
exe 'vert 1resize ' . ((&columns * 92 + 94) / 189)
exe 'vert 2resize ' . ((&columns * 96 + 94) / 189)
tabnext
edit ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/image_handle.py
tcd ~/Documents/Coding_Projects/Currently_Working/ColorGenerator
argglobal
balt ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/main.py
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 46 - ((32 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 46
normal! 013|
tabnext
edit ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/templates/base.html
tcd ~/Documents/Coding_Projects/Currently_Working/ColorGenerator
argglobal
balt ~/Documents/Coding_Projects/Currently_Working/ColorGenerator/templates/index.html
setlocal fdm=indent
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
5
normal! zo
5
normal! zo
14
normal! zo
15
normal! zo
17
normal! zo
21
normal! zo
22
normal! zo
23
normal! zo
26
normal! zo
29
normal! zo
32
normal! zo
39
normal! zo
41
normal! zo
42
normal! zo
43
normal! zo
52
normal! zo
53
normal! zo
54
normal! zo
55
normal! zo
56
normal! zo
let s:l = 29 - ((28 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 29
normal! 037|
tabnext 2
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
