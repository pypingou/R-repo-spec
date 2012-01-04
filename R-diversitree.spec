%global packname  diversitree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          diversitree: comparative phylogenetic tests of diversification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-deSolve R-ape R-subplex 


BuildRequires:    R-devel tex(latex) R-deSolve R-ape R-subplex



%description
Contains a number of comparative phylogenetic methods, mostly focussing on
analysing diversification and character evolution.  Contains
implementations of BiSSE (Binary State Speciation and Extinction; Maddison
et al. 2007: Syst. Biol. 56: 701) and its unresolved tree extensions
(FitzJohn et al. 2009: Syst. Biol. 58: 595), MuSSE (Multiple State
Speciation and Extinction), QuaSSE (Quantitative State Speciation and
Extinction; FitzJohn 2010: Syst. Biol. 69: 619), and GeoSSE (Geographic
State Speciation and Extinction; Goldberg et al. 2011: Syst. Biol.). Other
included methods include Markov models of discrete and continuous trait
evolution and constant rate speciation and extinction.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.2-1
- initial package for Fedora