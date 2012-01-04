%global packname  cMAP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.15.1
Release:          1%{?dist}
Summary:          A data package containing annotation data for cMAP

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Annotation data file for cMAP assembled using data from public data

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
%doc %{rlibdir}/cMAP/DESCRIPTION
%doc %{rlibdir}/cMAP/html
%{rlibdir}/cMAP/help
%{rlibdir}/cMAP/INDEX
%{rlibdir}/cMAP/Meta
%{rlibdir}/cMAP/NAMESPACE
%{rlibdir}/cMAP/R
%{rlibdir}/cMAP/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.15.1-1
- initial package for Fedora