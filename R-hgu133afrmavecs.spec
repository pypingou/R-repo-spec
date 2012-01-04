%global packname  hgu133afrmavecs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Vectors used by frma for microarrays of type hgu133a

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package was created by frmaTools version 1.3.11.

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
%doc %{rlibdir}/hgu133afrmavecs/DESCRIPTION
%doc %{rlibdir}/hgu133afrmavecs/html
%{rlibdir}/hgu133afrmavecs/help
%{rlibdir}/hgu133afrmavecs/data
%{rlibdir}/hgu133afrmavecs/Meta
%{rlibdir}/hgu133afrmavecs/INDEX
%{rlibdir}/hgu133afrmavecs/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8-1
- initial package for Fedora