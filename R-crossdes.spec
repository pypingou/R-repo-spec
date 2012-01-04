%global packname  crossdes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.9
Release:          1%{?dist}
Summary:          Design and Randomization in Crossover Studies

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-AlgDesign R-gtools R-MASS 

BuildRequires:    R-devel tex(latex) R-AlgDesign R-gtools R-MASS 

%description
Contains functions for the construction and randomization of balanced
carryover balanced designs. Contains functions to check given designs for
balance. Also contains functions for simulation studies on the validity of
two randomization procedures.

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
%doc %{rlibdir}/crossdes/DESCRIPTION
%doc %{rlibdir}/crossdes/html
%{rlibdir}/crossdes/NAMESPACE
%{rlibdir}/crossdes/Meta
%{rlibdir}/crossdes/R
%{rlibdir}/crossdes/INDEX
%{rlibdir}/crossdes/data
%{rlibdir}/crossdes/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.9-1
- initial package for Fedora