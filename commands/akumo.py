#!/usr/bin/env python3
import sys

# ANSI color codes
BOLD = "\033[1m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
CYAN = "\033[36m"
BRIGHT_YELLOW = "\033[93m"
RESET = "\033[0m"  # Resets text to default color

def draw_pumbaa():
    art = (
        "                            ,$\n"
        "                            dP,$\n"
        "                            $F<$b\n"
        "  ,;!!!!-                   $F<$$b         <  ,   ;\n"
        " ;!!!!'   ?                 `?.\"$$c      `;,`!<!!;`>   >\n"
        "!!!!!!    `?                   - \"?h,   .  `!,`!!;\\'  <>\n"
        "!!!!>>     `h                `-`- . \"r .,J,-'!>`>` !>,! !\n"
        "`!!! \\      3           ,ccc,,,.````,c$???$c`!!,`> ! !,'            ,r\n"
        " !!>        ?,          `$$$$$$$c$$$c,   ),$b`'` \\ `:'        ,,cc$$\"\n"
        "  `!        `h         -.`$PF\"$????$$$b,\"'?$$$J$c `'  ,,ccc$$$$$$P\"\n"
        "             F       -```,nP c$$$,<,3$$$$$$$$$$$$$$$$Ccd$$c`??\"\"\n"
        "            ;F        ,nMM\" $$$$$$ $$$$$$$$$$$$$$$$$$\"  ,`$\n"
        "            J'      ,MMMM  ,$$$$$'J$$$$$$$$$$$$$$$$$$ ,,,cc,,\n"
        "           ,$     JMMMMM `$$$$P\",$$$$$$$$$$$$$$$$$$$$b ?F<$hd$$P\"\n"
        "           JP    ,MMMMMM..\"L,,=$$$$$$$$$$$$$F\",;;,`\"??h, $$$P\"\n"
        "           $F    `MMMMMMb`,`\"?h,. ,$$$$$$$$$FF\"\"`\"\"\"\"==?-`?$\"\n"
        "          ,$      4MMMMMMb`Tnx`?$$$$$$$$$$$$$?????\"\"\"\"\"' .,,cc,            M\n"
        "          J$F    ,`4MMMMMMMh.(\\'$$$$$$PF\"',cccd$$$$$$$$$$$$$$$$$,         JM\n"
        "          ?\",,cP,$h,`4MMMMMMMMM $$$$P\",$$$$$$$$$$$$$$$$$$$$$$$$$$,     , ,MM\n"
        "        ,cd$$$$ d$$$$c,`\"4MMMMM,`$$$ J$$$$$$$$P\".::::,$$$$$$$$$$$$ ,,r\",nMMM\n"
        "      z$$$$$$$F $$$$$$$$$cc,. \"\" `$$ $$$$$$$$\":::`.:,$$$$$$$P\".`$$ ,xnMMMMP\n"
        "     d$$$$$$$$F $$$$$$$$$$$$$$$c   \">$`$$$$$$$, ```,z$$$$$$$\"::',$\",MMMMMP\"\n"
        "     $?$$$$$$$F $$$$$$$$$$$$$$$$L :::.\"\"??$$$$$$$$$$$$$$$$$c,,cP\" TTTT\"\n"
        "    j\"d$$$$$$$L $$$$$$$$$$$$$$$$$$,``,mn,_ .`\"\"\"???????????\"\"\" ,c\n"
        "     d$$$$$$$$$ ?$$$$$$$$$$$$$$$$$$b,`\"4MM,:::::..::::: ::: 3$c`\"\n"
        "   ,$$$$$$$$$$$c $$$$$$$$$$$$$$$$$$$$$c,.'  ::::::::::` ::::.\"?h,\n"
        " ,c$$$$$$$$$$ $$$c`$$$$$$$$$$$$$$$$$$$$$$$$$hcc,,,,.   ```..,,ccd$\"\n"
        " ',c\"?$$$$$$F,$$$$bd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'\n"
        " <$h`$$$$$\",$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P'\n"
        " `$$$c\".?$F,$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P\"\n"
        "  `$$$c,.\" d$$$$$$$$$$$$$$$$$,?$$$$$$$$$$$$$$$$$$$$$$$$$$$$P\"\n"
        "   `$$$$$c``$$$$$$$$$$$$$c\"$$$c\"$$$$$$$$$$$$$$$$$$$$$$$$P\"\n"
        "    `?$$$$h,`$$$$$$$$$$$$$h,?$$h,\"$$$$$$$$$$$$$$$$$$PF\".\n"
        "      \"$$$$$h ?$$$$$$$$F$$$$$c`??$c,\"?$$$$$$$$$$P\"',c$\"\n"
        "      -,\"?$$$$,\"$$$$$$$b`$$$$$$hc,`\"\"==    .,,,cd$$P\",\n"
        "       \"$c,\"??$h \"$$$$$$c`\"==- ,z$$$$$$$$$$c-`3$P\",c$\"\n"
        "        `$$$c  \"\"- ?$$$$$ J$$$$$$$$$$$$$$$$$$ \",c$$P'\n"
        "          ?$$       \"$$$$ ???$$$$$$$$$$$$PF\" z$$$P\"\n"
        "           `$        `$$\"       ,,           $$$\"\n"
        "            $>        ?$        `$           4$'\n"
        "           ,F         ?$         \"P  ,       4F\n"
        "         ???'         `$           4Mn`-     J(\n"
        "                       $c                    $b,\n"
        "                   ,- ???                    `,dn(+\n"
        "                  ',dMM-                      `\"??=\n"
        "                   \"\n"
    )
    print(art)


def main():
    try:

        MARGIN_LEFT = "   "
        MARGIN_TOP = "\n"
        MARGIN_BOTTOM = "\n\n\n"
        OUTPUT_TITLE = f"{MARGIN_LEFT}{RED}THE OUTPUT:{RESET}\n"

        # Check if arguments are provided
        if len(sys.argv) > 1:
            input_text = " ".join(sys.argv[1:])  # Use command-line arguments as input
            print(f"{MARGIN_TOP}{MARGIN_LEFT}{BOLD}Akumo Matata{RESET} – No Worries, Just Learning ☁️⛅🌤!{MARGIN_TOP}")
            print(OUTPUT_TITLE)
            print(f"{MARGIN_LEFT}{input_text}")
        elif not sys.stdin.isatty():  # Check if input is coming from a pipe (the Output)
            input_text = sys.stdin.read().strip()
            # Print ASCII art first
            draw_pumbaa()
            print(OUTPUT_TITLE)
            print(f"{MARGIN_LEFT}{GREEN}{input_text}{RESET}{MARGIN_BOTTOM}")
        else:
            input_text = f"{MARGIN_TOP}{MARGIN_LEFT}Where is {BOLD}prompt{RESET} ?{MARGIN_TOP}{MARGIN_LEFT}👀{MARGIN_TOP}{MARGIN_LEFT}Baby don't hurt me, don't hurt me, no more.💔❤️‍🩹😭🎶"
            print(f"{MARGIN_LEFT}{input_text}{MARGIN_BOTTOM}")
        
        print(RESET)

    except KeyboardInterrupt:
        print("\n[Process interrupted. No worries, Hakuna Matata!]\n")
        sys.exit(0)

if __name__ == "__main__":
    main()

