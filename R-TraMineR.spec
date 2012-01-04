%global packname  TraMineR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.1
Release:          1%{?dist}
Summary:          Sequences and trajectories mining for social scientists

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RColorBrewer R-boot 


BuildRequires:    R-devel tex(latex) R-RColorBrewer R-boot



%description
This package is a toolbox for sequence manipulation, description,
rendering and more generally sequence data mining in the field of social
sciences. Though it is primarily intended for analyzing state or event
sequences that describe life courses such as family formation histories or
professional careers its features apply indeed also to many other kinds of
categorical sequence data. It accepts as input many different sequence
representations and provides tools for translating sequences from one
format to another. It offers several statistical functions for describing
and rendering sequences, for computing distances between sequences with
different metrics among which optimal matching, the longest common prefix
and the longest common subsequence, and simple functions for extracting
the most frequent subsequences and identifying the most discriminating
ones among them. A user's guide can be found on TraMineR's web page.

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
%doc %{rlibdir}/TraMineR/CITATION
%doc %{rlibdir}/TraMineR/NEWS
%doc %{rlibdir}/TraMineR/DESCRIPTION
%doc %{rlibdir}/TraMineR/html
%{rlibdir}/TraMineR/INDEX
%{rlibdir}/TraMineR/R
%{rlibdir}/TraMineR/demo
%{rlibdir}/TraMineR/NAMESPACE
%{rlibdir}/TraMineR/data
%{rlibdir}/TraMineR/Meta
%{rlibdir}/TraMineR/help
%{rlibdir}/TraMineR/libs

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.1-1
- initial package for Fedora