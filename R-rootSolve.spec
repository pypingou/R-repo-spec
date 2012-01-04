%global packname  rootSolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.2
Release:          1%{?dist}
Summary:          Nonlinear root finding, equilibrium and steady-state analysis of ordinary differential equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Routines to find the root of nonlinear functions, and to perform
steady-state and equilibrium analysis of ordinary differential equations
(ODE). Includes routines that: (1) generate gradient and Jacobian matrices
(full and banded), (2) find roots of non-linear equations by the
Newton-Raphson method, (3) estimate steady-state conditions of a system of
(differential) equations in full, banded or sparse form, using the
Newton-Raphson method, or by dynamically running, (4) solve the
steady-state conditions for uni-and multicomponent 1-D, 2-D, and 3-D
partial differential equations, that have been converted to ODEs by
numerical differencing (using the method-of-lines approach). Includes
fortran code.

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
%doc %{rlibdir}/rootSolve/doc
%doc %{rlibdir}/rootSolve/DESCRIPTION
%doc %{rlibdir}/rootSolve/html
%doc %{rlibdir}/rootSolve/CITATION
%{rlibdir}/rootSolve/libs
%{rlibdir}/rootSolve/R
%{rlibdir}/rootSolve/Meta
%{rlibdir}/rootSolve/help
%{rlibdir}/rootSolve/INDEX
%{rlibdir}/rootSolve/demo
%{rlibdir}/rootSolve/dynload
%{rlibdir}/rootSolve/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.2-1
- initial package for Fedora