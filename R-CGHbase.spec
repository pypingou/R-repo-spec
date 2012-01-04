%global packname  CGHbase
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          CGHbase: Base functions and classes for arrayCGH data analysis.

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-Biobase R-marray 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-marray 

%description
Contains functions and classes that are needed by arrayCGH packages.

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
%doc %{rlibdir}/CGHbase/DESCRIPTION
%doc %{rlibdir}/CGHbase/html
%{rlibdir}/CGHbase/help
%{rlibdir}/CGHbase/Meta
%{rlibdir}/CGHbase/R
%{rlibdir}/CGHbase/data
%{rlibdir}/CGHbase/INDEX
%{rlibdir}/CGHbase/NAMESPACE

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora