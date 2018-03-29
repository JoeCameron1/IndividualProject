% =============================================================================
% l4proj.cls
%
% Template for final year projects in the School of Computing Science at the
% University of Glasgow. Adapted from the level 3 project template originally
% provided by Colin Perkins <csp@dcs.gla.ac.uk>.
%
% =============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{l4proj}[%
2009/01/09 Colin Perkins <csp@dcs.gla.ac.uk>.%
2009/09/16 Modified by Tim Storer <tws@dcs.gla.ac.uk> to support non pdf modes.%
2011/02/15 Modified by Gregg Hamilton <hamiltgr@dcs.gla.ac.uk> for use in final year projects.%
2012/10/18 Modified by Patrick Prosser, use geometry to control margins, simplified.%
]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions
\LoadClass[11pt,a4paper]{report}

\usepackage{ifpdf}
\ifpdf
\usepackage[pdftex]{graphicx}
\else
\usepackage{graphicx}
\fi

\usepackage[toc,page]{appendix}
\usepackage{times}
\usepackage[top=3.5cm,bottom=4cm]{geometry}
\setlength{\parskip}{11pt plus 2pt}

\renewcommand\maketitle{\begin{titlepage}%
\let\footnotesize\small
\let\footnoterule\relax
\let\footnote \thanks
\vspace{1in}
\includegraphics[trim=1.0cm 1.0cm 1.0cm 1.0cm]{images/CompSci_colour}
\vspace{2cm}
  \Large
  \vskip 8em%
  \noindent
  {\LARGE \@title \par}%
  \vskip 3em%
  \large
  \lineskip .75em%
  \noindent
  \begin{tabular}[t]{@{}l}%
    \@author
  \end{tabular}\par%
  \vskip 3em%
  \noindent
  School of Computing Science\\
  Sir Alwyn Williams Building\\
  University of Glasgow\\
  G12 8QQ
  \Large
  \vskip 6em%
  \noindent
  Level 4 Project --- \@date 
  \vfill
\end{titlepage}%
\setcounter{footnote}{0}%
\global\let\thanks\relax
\global\let\maketitle\relax
\global\let\@thanks\@empty
\global\let\@author\@empty
\global\let\@date\@empty
\global\let\@title\@empty
\global\let\title\relax
\global\let\author\relax
\global\let\date\relax
\global\let\and\relax
}

\newcommand{\educationalconsent}{
\newpage
\section*{Education Use Consent}

I hereby give my permission for this project to be shown to other
University of Glasgow students and to be distributed in an electronic
format.  \textbf{Please note that you are under no obligation to sign 
this declaration, but doing so would help future students.}

\begin{tabular}{@{}llll}
      &                     &            &                     \\
      &                     &            &                     \\
Name: & \rule{4.0cm}{0.5mm} & Signature: & \rule{4.5cm}{0.5mm} \\
      &                     &            &                     \\
      &                     &            &                     \\
\end{tabular}
}

\addtolength\textwidth{1.0in}
\addtolength\oddsidemargin{-0.50in}
\addtolength\textheight{1.0in}
\addtolength\topmargin{-0.5in}

\pagenumbering{roman}