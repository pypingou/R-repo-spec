%global packname  limSolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Solving Linear Inverse Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-quadprog R-lpSolve R-MASS 

BuildRequires:    R-devel tex(latex) R-quadprog R-lpSolve R-MASS 

%description
Functions that (1.) Find the minimum/maximum of a linear or quadratic
function: min or max (f(x)), where f(x) = ||Ax-b||^2 or f(x) = sum(ai*xi)
subject to equality constraints Ex=f and/or inequality constraints Gx>=h.
(2.) Sample an underdetermined- or overdetermined system Ex=f subject to
Gx>=h, and if applicable Ax~=b. (3.) Solve a linear system Ax=B for the
unknown x. Includes banded and tridiagonal linear systems. The package
calls Fortran functions from LINPACK

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
%doc %{rlibdir}/limSolve/CITATION
%doc %{rlibdir}/limSolve/html
%doc %{rlibdir}/limSolve/doc
%doc %{rlibdir}/limSolve/DESCRIPTION
%{rlibdir}/limSolve/libs
%{rlibdir}/limSolve/data
%{rlibdir}/limSolve/demo
RPM build errors:
%{rlibdir}/limSolve/INDEX
%{rlibdir}/limSolve/NAMESPACE
%{rlibdir}/limSolve/help
%{rlibdir}/limSolve/R
%{rlibdir}/limSolve/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.2-1
- initial package for Fedora