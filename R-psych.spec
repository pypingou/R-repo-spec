%global packname  psych
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1111
Release:          1%{?dist}
Summary:          Procedures for Psychological, Psychometric, and Personality Research

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A number of routines for personality, psychometrics and experimental
psychology.   Functions are primarily for scale construction using factor
analysis, cluster analysis and reliability analysis, although others
provide basic descriptive statistics. Item Response Theory is done using 
factor analysis of tetrachoric and polychoric correlations. Functions for
simulating particular item and test structures are included. Several
functions serve as a useful front end for structural equation modeling. 
Graphical displays of path diagrams, factor analysis and structural
equation models are created using basic graphics. Some of the functions
are written to support a book on psychometrics as well as publications in
personality research. For more information, see the
personality-project.org/r webpage.

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
%doc %{rlibdir}/psych/doc
%doc %{rlibdir}/psych/DESCRIPTION
%doc %{rlibdir}/psych/html
%doc %{rlibdir}/psych/CITATION
%{rlibdir}/psych/data
%{rlibdir}/psych/Meta
%{rlibdir}/psych/NEWS.Rd
%{rlibdir}/psych/R
%{rlibdir}/psych/INDEX
RPM build errors:
%{rlibdir}/psych/help
%{rlibdir}/psych/NAMESPACE

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1111-1
- initial package for Fedora