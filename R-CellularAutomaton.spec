%global packname  CellularAutomaton
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          One-Dimensional Cellular Automata

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.oo 

BuildRequires:    R-devel tex(latex) R-R.oo 

%description
This package is an object-oriented implementation of one-dimensional
cellular automata. It supports many of the features offered by
Mathematica, including elementary rules, user-defined rules, radii,
user-defined seeding, and plotting.

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
%doc %{rlibdir}/CellularAutomaton/DESCRIPTION
%doc %{rlibdir}/CellularAutomaton/html
%{rlibdir}/CellularAutomaton/R
%{rlibdir}/CellularAutomaton/INDEX
%{rlibdir}/CellularAutomaton/Meta
%{rlibdir}/CellularAutomaton/help

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora