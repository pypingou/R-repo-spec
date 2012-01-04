%global packname  HH
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.17
Release:          1%{?dist}
Summary:          Statistical Analysis and Data Display: Heiberger and Holland

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-stats R-grid R-multcomp R-mvtnorm R-methods R-leaps R-RColorBrewer R-latticeExtra 

BuildRequires:    R-devel tex(latex) R-lattice R-stats R-grid R-multcomp R-mvtnorm R-methods R-leaps R-RColorBrewer R-latticeExtra 

%description
Support software for Statistical Analysis and Data Display (Springer, ISBN
0-387-40270-5).  This contemporary presentation of statistical methods
features extensive use of graphical displays for exploring data and for
displaying the analysis. The authors demonstrate how to analyze
data---showing code, graphics, and accompanying computer listings---for
all the methods they cover. They emphasize how to construct and interpret
graphs, discuss principles of graphical design, and show how accompanying
traditional tabular results are used to confirm the visual impressions
derived directly from the graphs. Many of the graphical formats are novel
and appear here for the first time in print. All chapters have exercises.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.17-1
- initial package for Fedora