%global packname  hgu133plus2frmavecs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Vectors used by frma for microarrays of type hgu133plus2

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package was created by frmaTools version 1.3.4.

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
%doc %{rlibdir}/hgu133plus2frmavecs/DESCRIPTION
%doc %{rlibdir}/hgu133plus2frmavecs/html
%{rlibdir}/hgu133plus2frmavecs/data
%{rlibdir}/hgu133plus2frmavecs/help
%{rlibdir}/hgu133plus2frmavecs/NAMESPACE
%{rlibdir}/hgu133plus2frmavecs/INDEX
%{rlibdir}/hgu133plus2frmavecs/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8-1
- initial package for Fedora