%global packname  affycompData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          affycomp data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase 

%description
Data needed by the affycomp package.

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
%doc %{rlibdir}/affycompData/DESCRIPTION
%doc %{rlibdir}/affycompData/html
%{rlibdir}/affycompData/INDEX
%{rlibdir}/affycompData/Meta
%{rlibdir}/affycompData/data
%{rlibdir}/affycompData/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora