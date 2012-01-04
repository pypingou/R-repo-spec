%global packname  nugohs1a520180cdf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.4.1
Release:          1%{?dist}
Summary:          nugohs1a520180cdf

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
A package containing an environment representing the NuGO_Hs1a520180.cdf

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
%doc %{rlibdir}/nugohs1a520180cdf/DESCRIPTION
%doc %{rlibdir}/nugohs1a520180cdf/html
%{rlibdir}/nugohs1a520180cdf/R
%{rlibdir}/nugohs1a520180cdf/NAMESPACE
%{rlibdir}/nugohs1a520180cdf/INDEX
%{rlibdir}/nugohs1a520180cdf/Meta
%{rlibdir}/nugohs1a520180cdf/help
%{rlibdir}/nugohs1a520180cdf/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.1-1
- initial package for Fedora