%global packname  lpSolveAPI
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.5.2.0.5
Release:          1%{?dist}
Summary:          R Interface for lp_solve version 5.5.2.0

Group:            Applications/Engineering 
License:          LGPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_5.5.2.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The lpSolveAPI package provides an R interface for lp_solve, a Mixed
Integer Linear Programming (MILP) solver with support for pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS)

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
%doc %{rlibdir}/lpSolveAPI/html
%doc %{rlibdir}/lpSolveAPI/DESCRIPTION
%doc %{rlibdir}/lpSolveAPI/doc
%{rlibdir}/lpSolveAPI/Meta
%{rlibdir}/lpSolveAPI/tests
%{rlibdir}/lpSolveAPI/lpSolve
%{rlibdir}/lpSolveAPI/libs
%{rlibdir}/lpSolveAPI/include
%{rlibdir}/lpSolveAPI/R
%{rlibdir}/lpSolveAPI/INDEX
RPM build errors:
%{rlibdir}/lpSolveAPI/NAMESPACE
%{rlibdir}/lpSolveAPI/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.5.2.0.5-1
- initial package for Fedora