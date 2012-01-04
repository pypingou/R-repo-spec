%global packname  granovaGG
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Graphical Analysis of Variance Using ggplot2

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ggplot2 R-RColorBrewer R-gridExtra R-MASS 

BuildRequires:    R-devel tex(latex) R-ggplot2 R-RColorBrewer R-gridExtra R-MASS 

%description
This collection of functions in granovaGG provides what we call elemental
graphics for display of anova results. The term elemental derives from the
fact that each function is aimed at construction of graphical displays
that afford direct visualizations of data with respect to the fundamental
questions that drive the particular anova methods. This package represents
a modification of the original granova package; the key change is to use
ggplot2, Hadley Wickham's package based on Grammar of Graphics concepts
(due to Wilkinson). The main function is granovagg.1w (a graphic for one
way anova); two other functions (granovagg.ds and granovagg.contr) are to
construct graphics for dependent sample analyses and contrast-based
analyses respectively. (The function granova.2w, which entails dynamic
displays of data, is not currently part of granovaGG.) The granovaGG
functions are to display data for any number of groups, regardless of
their sizes (however, very large data sets or numbers of groups can be
problematic). For granovagg.1w a specialized approach is used to construct
data-based contrast vectors for which anova data are displayed. The result
is that the graphics use a straight line to facilitate clear
interpretations while being faithful to the standard effect test in anova.
The graphic results are complementary to standard summary tables; indeed,
numerical summary statistics are provided as side effects of the graphic
constructions. granovagg.ds and granovagg.contr provide graphic displays
and numerical outputs for a dependent sample and contrast-based analyses.
The graphics based on these functions can be especially helpful for
learning how the respective methods work to answer the basic question(s)
that drive the analyses. This means they can be particularly helpful for
students and non-statistician analysts. But these methods can be of
assistance for work-a-day applications of many kinds, as they can help to
identify outliers, clusters or patterns, as well as highlight the role of
non-linear transformations of data. In the case of granovagg.1w and
granovagg.ds several arguments are provided to facilitate flexibility in
the construction of graphics that accommodate diverse features of data,
according to their corresponding display requirements. See the help files
for individual functions.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora