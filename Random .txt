@echo off
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Variables::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
color 0A
set /a NUM=%random% %%100 +1
for /f %%a in ('date /t') do set WEEKDAY=%%a
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "datestamp=%YYYY%%MM%%DD%" & set "timestamp=%HH%%Min%%Sec%"
set "fullstamp=%YYYY%-%MM%-%DD%_%HH%-%Min%-%Sec%"
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Testing::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::
echo.
echo fullstamp: "%fullstamp%"
::echo datestamp: "%datestamp%"
::echo timestamp: "%timestamp%"
echo Today is %WEEKDAY%
echo Day #%DD%
echo Random# is %NUM%
echo.
echo.
timeout /T 2
::


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Standard Sites for everyday use::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::1 second timeout added to open every page; this sets predictable opening order:::::::::::::::::
:::::::::::::::::will also limit whiteflash when switching pages if using dark reader extension:::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
start /min "" http://slickdeals.net/
timeout /T 1
start /min "" http://www.visualcapitalist.com/
timeout /T 1
start /min "" http://www.history.com/this-day-in-history
timeout /T 1
start "" http://www.marketwatch.com/
timeout /T 1
start "" http://www.tutsnode.net/
timeout /T 1
start "" https://www.zerohedge.com/
timeout /T 1

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Weekday sites, open only on set day of the week::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
IF %WEEKDAY%==Mon GOTO :mon
IF %WEEKDAY%==Tue GOTO :tue
IF %WEEKDAY%==Wed GOTO :wed
IF %WEEKDAY%==Thu GOTO :thu
IF %WEEKDAY%==Fri GOTO :fri
IF %WEEKDAY%==Sat GOTO :sat
IF %WEEKDAY%==Sun GOTO :sun

:mon
echo %WEEKDAY%
start "" http://www.carolinahuddle.com/boards/forum/7-carolina-panthers-news-and-talk/
timeout /T 1
GOTO DAYOFMONTH

:tue
echo %WEEKDAY%
start "" http://www.espn.com/fantasy/football/
timeout /T 1
GOTO DAYOFMONTH

:wed
echo %WEEKDAY%
start "" http://www.imdb.com/movies-in-theaters/
timeout /T 1
GOTO DAYOFMONTH

:thu
echo %WEEKDAY%
start "" https://www.youtube.com/user/2theRedlineLLC/videos
timeout /T 1
GOTO DAYOFMONTH

:fri
echo %WEEKDAY%
start "" http://www.doctorofcredit.com/
timeout /T 1
GOTO DAYOFMONTH

:sat
echo %WEEKDAY%
start "" http://www.bbc.com/future/columns/best-of-the-web
timeout /T 1
GOTO DAYOFMONTH

:sun
echo %WEEKDAY%
start "" https://futurism.com/
timeout /T 1
start "" https://www.livescience.com/50718-weekend-reading.html
timeout /T 1
GOTO DAYOFMONTH

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::One day a month sites, open only on set day of the month:::::::::::::::::::::::::::::::::::::::
:::::::::::::::::uses DD for variable and labels::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:DAYOFMONTH
echo %DD%
IF %DD% EQU 1 GOTO DD1
IF %DD% EQU 1 GOTO DD2
IF %DD% EQU 1 GOTO DD3
IF %DD% EQU 1 GOTO DD4
IF %DD% EQU 1 GOTO DD5
IF %DD% EQU 1 GOTO DD6
IF %DD% EQU 1 GOTO DD7
IF %DD% EQU 1 GOTO DD8
IF %DD% EQU 1 GOTO DD9
IF %DD% EQU 1 GOTO DD10
IF %DD% EQU 1 GOTO DD11
IF %DD% EQU 1 GOTO DD12
IF %DD% EQU 1 GOTO DD13
IF %DD% EQU 1 GOTO DD14
IF %DD% EQU 1 GOTO DD15
IF %DD% EQU 1 GOTO DD16
IF %DD% EQU 1 GOTO DD17
IF %DD% EQU 1 GOTO DD18
IF %DD% EQU 1 GOTO DD19
IF %DD% EQU 1 GOTO DD20
IF %DD% EQU 1 GOTO DD21
IF %DD% EQU 1 GOTO DD22
IF %DD% EQU 1 GOTO DD23
IF %DD% EQU 1 GOTO DD24
IF %DD% EQU 1 GOTO DD25
IF %DD% EQU 1 GOTO DD26
IF %DD% EQU 1 GOTO DD27
IF %DD% EQU 1 GOTO DD28
IF %DD% EQU 1 GOTO DD28
IF %DD% EQU 1 GOTO DD30
IF %DD% EQU 1 GOTO DD31

:DD1
start "" https://www.creditkarma.com/
timeout /T 1
GOTO randomchance
:DD2
start "" https://www.mauldineconomics.com/

GOTO randomchance
:DD3
GOTO randomchance
:DD4
GOTO randomchance
:DD5
GOTO randomchance
start "" https://www.fly.com/todaysbestfares
timeout /T 1
:DD6
GOTO randomchance
:DD7
GOTO randomchance
:DD8
GOTO randomchance
:DD9
GOTO randomchance
:DD10
GOTO randomchance
:DD11
GOTO randomchance
:DD12
GOTO randomchance
:DD13
GOTO randomchance
:DD14
GOTO randomchance
:DD15
start ""  http://www.eflens.com/lens_articles/canon_lens_date_codes.html
timeout /T 1
GOTO randomchance
:DD16
GOTO randomchance
:DD17
GOTO randomchance
:DD18
GOTO randomchance
:DD19
GOTO randomchance
:DD20
start "" https://twitter.com/NASANewHorizons
timeout /T 1
GOTO randomchance
:DD21
GOTO randomchance
:DD22
GOTO randomchance
:DD23
GOTO randomchance
:DD24
GOTO randomchance
:DD25
GOTO randomchance
:DD26
GOTO randomchance
:DD27
GOTO randomchance
:DD28
start "" http://www.doctorofcredit.com/best-current-credit-card-sign-bonuses/
timeout /T 1
GOTO randomchance
:DD29
GOTO randomchance
:DD30
GOTO randomchance
:DD31
GOTO randomchance

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Random Sites:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Random Chance Sites::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::50% chance of not opening any sites, as 1-50 skip Chance sites and goto random10 sites:::::::::
:::::::::::::::::50% of opening the over50 sites 51-100, sites you don't mind viewing rather often::::::::::::::
:::::::::::::::::10% chance of opening over90 sites 91-100, additional random sites you dont want often:::::::::
:::::::::::::::::This isn't exactly 50-50 technically but who cares?  It's close enough!::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Random Chance Testing, will get Sites 50% of time, label Over50::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:randomchance
IF %NUM% GTR 50 GOTO over50
echo You're under 50
GOTO random10

:over50
echo You're over 50
::List sites you want to show about half the time
start "" https://camelcamelcamel.com/top_drops
timeout /T 1
start "" http://www.businessinsider.com/trending
timeout /T 1

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Random Chance Sites 10% of time, label Over90::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
IF %NUM% GTR 90 GOTO over90
GOTO random10

:over90
echo you're over 90
::List sites you want to show about 10% of the time
start "" https://futuristech.info/
timeout /T 1
start "" http://www.sportofusa.com/
timeout /T 1
start "" http://lifehacker.com/
timeout /T 1

GOTO random10

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::Random 10+ Sites, Your single random site::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::To add more sites, increase the set %%#, add a IF EQU #, add a :#, start and GOTO statement::::
:::::::::::::::::Example for #21 is provided below, leave label "random10" alone for consistency::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:random10
set /a randomsite=%random% %%20 +1
::set /a randomsite=%random% %%21 +1
IF %randomsite% EQU 1 GOTO 1
IF %randomsite% EQU 2 GOTO 2
IF %randomsite% EQU 3 GOTO 3
IF %randomsite% EQU 4 GOTO 4
IF %randomsite% EQU 5 GOTO 5
IF %randomsite% EQU 6 GOTO 6
IF %randomsite% EQU 7 GOTO 7
IF %randomsite% EQU 8 GOTO 8
IF %randomsite% EQU 9 GOTO 9
IF %randomsite% EQU 10 GOTO 10
IF %randomsite% EQU 11 GOTO 11
IF %randomsite% EQU 12 GOTO 12
IF %randomsite% EQU 13 GOTO 13
IF %randomsite% EQU 14 GOTO 14
IF %randomsite% EQU 15 GOTO 15
IF %randomsite% EQU 16 GOTO 16
IF %randomsite% EQU 17 GOTO 17
IF %randomsite% EQU 18 GOTO 18
IF %randomsite% EQU 19 GOTO 19
IF %randomsite% EQU 20 GOTO 20
::IF %randomsite% EQU 21 GOTO 21

:1
start "" https://www.reddit.com/r/Futurology/
GOTO endrandom10
:2
start "" https://twitter.com/jjones9
GOTO endrandom10
:3
start "" https://twitter.com/roaringriot
GOTO endrandom10
:4
start "" https://waitbutwhy.com/random/
GOTO endrandom10
:5
start "" http://www.spanishdict.com/wordoftheday/random
GOTO endrandom10
:6
start "" https://arstechnica.com/
GOTO endrandom10
:7
start "" http://wfae.org/programs/charlotte-talks-wfae
GOTO endrandom10
:8
start "" http://www.pslsource.com/buy_carolina_panthers_psl/
GOTO endrandom10
:9
start "" http://www.coolthings.com/
GOTO endrandom10
:10
start "" https://www.reddit.com/r/random/
GOTO endrandom10
:11
start "" https://imgur.com/gallery/m5PMjWb
GOTO endrandom10
:12
start "" http://lifehacker.com/
GOTO endrandom10
:13
start "" http://www.wbur.org/onpoint/archive
GOTO endrandom10
:14
start "" https://www.reddit.com/r/EarthPorn/
GOTO endrandom10
:15
start "" http://phandroid.com/
GOTO endrandom10
:16
start "" https://www.creditkarma.com/
GOTO endrandom10
:17
start "" https://www.muscleforlife.com/
timeout /T 1
:18
start "" https://www.theptdc.com/category/best-fitness-articles/
timeout /T 1
:19
start "" https://www.reddit.com/r/learnpython/hot/
GOTO endrandom10
:20
start "" http://wordsmith.org/words/random.cgi
GOTO endrandom10

:::21
::start "" http://wordsmith.org/words/random.cgi
::GOTO endrandom10


:endrandom10

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::