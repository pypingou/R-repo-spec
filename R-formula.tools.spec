%global packname  formula.tools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Utilities for working with formulas, expressions, calls and other R objects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-operator.tools R-utils R-methods 

BuildRequires:    R-devel tex(latex) R-operator.tools R-utils R-methods 

%description
This package provides a number of useful utilities for working with
formulas, expressions, calls, names, symbols and other R objects.  This
package was designed to greatly facilitate symbolic manupulation using
native R objects.

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
%doc %{rlibdir}/formula.tools/DESCRIPTION
%doc %{rlibdir}/formula.tools/html
%{rlibdir}/formula.tools/LICENSE
%{rlibdir}/formula.tools/NAMESPACE
%{rlibdir}/formula.tools/R
%{rlibdir}/formula.tools/Meta
%{rlibdir}/formula.tools/INDEX
%{rlibdir}/formula.tools/help

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora