%global packname  beta7
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Rodriguez et al. (2004) Differential Gene Expression by Memory/Effector T Helper Cells Bearing the Gut-Homing Receptor Integrin alpha4 beta7.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-marray 

BuildRequires:    R-devel tex(latex) R-marray 

%description
Data from 6 gpr files aims to identify differential expressed genes
between the beta 7+ and beta 7- memory T helper cells.

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
%doc %{rlibdir}/beta7/html
%doc %{rlibdir}/beta7/DESCRIPTION
%{rlibdir}/beta7/INDEX
%{rlibdir}/beta7/help
%{rlibdir}/beta7/NAMESPACE
%{rlibdir}/beta7/Meta
%{rlibdir}/beta7/beta7
%{rlibdir}/beta7/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora