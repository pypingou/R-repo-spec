%global packname  gahgu95bcdf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          gahgu95bcdf

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
A package containing an environment representing the gahgu95b.cdf file.

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
%doc %{rlibdir}/gahgu95bcdf/html
%doc %{rlibdir}/gahgu95bcdf/DESCRIPTION
%{rlibdir}/gahgu95bcdf/data
%{rlibdir}/gahgu95bcdf/NAMESPACE
%{rlibdir}/gahgu95bcdf/R
%{rlibdir}/gahgu95bcdf/Meta
%{rlibdir}/gahgu95bcdf/INDEX
%{rlibdir}/gahgu95bcdf/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.0-1
- initial package for Fedora