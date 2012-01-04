%global packname  GANPAdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          The GANPA Datasets Package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is a dataset package for GANPA, which implements a network-based gene
weighting approach to pathway analysis. This package includes data useful
for GANPA, such as a functional association network, pathways, an
expression dataset and multi-subunit proteins.

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
%doc %{rlibdir}/GANPAdata/html
%doc %{rlibdir}/GANPAdata/DESCRIPTION
%{rlibdir}/GANPAdata/INDEX
%{rlibdir}/GANPAdata/Meta
%{rlibdir}/GANPAdata/NAMESPACE
%{rlibdir}/GANPAdata/help
%{rlibdir}/GANPAdata/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora