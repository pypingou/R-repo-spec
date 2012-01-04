%global packname  Rd2roxygen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Convert Rd to roxygen documentation and utilities to improve documentation

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-roxygen2 R-formatR 

BuildRequires:    R-devel tex(latex) R-roxygen2 R-formatR 

%description
Functions to convert Rd to roxygen documentation. It can parse an Rd file
to a list, create the roxygen documentation and update the original R
script (e.g. the one containing the definition of the function)
accordingly. This package also provides utilities which can help
developers build packages using roxygen more easily. The formatR package
can be used to reformat the R code in the examples sections so that the
code will be more readable.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora