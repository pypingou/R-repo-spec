%global packname  breastCancerMAINZ
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Gene expression dataset published by Schmidt et al. [2008] (MAINZ).

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Gene expression data from the breast cancer study published by Schmidt et
al. in 2008, provided as an eSet.

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
%doc %{rlibdir}/breastCancerMAINZ/html
%doc %{rlibdir}/breastCancerMAINZ/DESCRIPTION
%{rlibdir}/breastCancerMAINZ/NAMESPACE
%{rlibdir}/breastCancerMAINZ/INDEX
%{rlibdir}/breastCancerMAINZ/data
%{rlibdir}/breastCancerMAINZ/help
%{rlibdir}/breastCancerMAINZ/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora