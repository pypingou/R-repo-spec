%global packname  lpSolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          5.6.6
Release:          1%{?dist}
Summary:          Interface to Lp_solve v. 5.5 to solve linear/integer programs

Group:            Applications/Engineering 
License:          LGPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Lp_solve is freely available (under LGPL 2) software for solving linear,
integer and mixed integer programs. In this implementation we supply a
"wrapper" function in C and some R functions that solve general
linear/integer problems, assignment problems, and transportation problems.
This version calls lp_solve version 5.5.

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
%doc %{rlibdir}/lpSolve/DESCRIPTION
%doc %{rlibdir}/lpSolve/html
%{rlibdir}/lpSolve/libs
%{rlibdir}/lpSolve/INDEX
%{rlibdir}/lpSolve/Meta
%{rlibdir}/lpSolve/R
%{rlibdir}/lpSolve/NAMESPACE
%{rlibdir}/lpSolve/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 5.6.6-1
- initial package for Fedora