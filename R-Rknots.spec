%global packname  Rknots
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Rknots

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rgl R-rSymPy 


BuildRequires:    R-devel tex(latex) R-rgl R-rSymPy



%description
The Rknots package contains functions for the topological analysis of
polymeric structures, either biological polymers or synthetic structures,
with a major focus on proteins. This release provides a Protein Data Bank
(PDB) entries import function, two structure reduction algorithms (MSR,
Minimal Structure Reduction and Alexander-Briggs reduction), polynomials
(Alexander, Jones and HOMFLY polynomial via Conway's skein triple) and
linking number computation, graphical functions and a set of utilities.
Credits are due to the bio3d package on which the PDB import function is
based, to the google code project SymPy that provides a Computer Algebra
System for Python and to the Rsympy package.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora