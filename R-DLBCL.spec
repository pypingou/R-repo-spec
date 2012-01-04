%global packname  DLBCL
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.3
Release:          1%{?dist}
Summary:          Diffuse large B-cell lymphoma expression data

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
This package provides additional expression data on diffuse large B-cell
lymphomas for the BioNet package.

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
%doc %{rlibdir}/DLBCL/html
%doc %{rlibdir}/DLBCL/DESCRIPTION
%{rlibdir}/DLBCL/Meta
%{rlibdir}/DLBCL/NAMESPACE
%{rlibdir}/DLBCL/help
%{rlibdir}/DLBCL/data
%{rlibdir}/DLBCL/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.3-1
- initial package for Fedora