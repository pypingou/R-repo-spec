%global packname  deSolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.3
Release:          1%{?dist}
Summary:          General solvers for initial value problems of ordinary differential equations (ODE), partial differential equations (PDE), differential algebraic equations (DAE), and delay differential equations (DDE).

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.10-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions that solve initial value problems of a system of first-order
ordinary differential equations (ODE), of partial differential equations
(PDE), of differential algebraic equations (DAE), and of delay
differential equations. The functions provide an interface to the FORTRAN
functions lsoda, lsodar, lsode, lsodes of the ODEPACK collection, to the
FORTRAN functions dvode and daspk and a C-implementation of solvers of the
Runge-Kutta family with fixed or variable time steps. The package contains
routines designed for solving ODEs resulting from 1-D, 2-D and 3-D partial
differential equations (PDE) that have been converted to ODEs by numerical

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
%doc %{rlibdir}/deSolve/CITATION
%doc %{rlibdir}/deSolve/doc
%doc %{rlibdir}/deSolve/html
%doc %{rlibdir}/deSolve/DESCRIPTION
%doc %{rlibdir}/deSolve/NEWS
%{rlibdir}/deSolve/INDEX
%{rlibdir}/deSolve/libs
%{rlibdir}/deSolve/help
%{rlibdir}/deSolve/Meta
%{rlibdir}/deSolve/data
%{rlibdir}/deSolve/demo
%{rlibdir}/deSolve/R
%{rlibdir}/deSolve/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.3-1
- initial package for Fedora