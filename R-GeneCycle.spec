%global packname  GeneCycle
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Identification of Periodically Expressed Genes

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-longitudinal R-fdrtool 

BuildRequires:    R-devel tex(latex) R-MASS R-longitudinal R-fdrtool 

%description
The GeneCycle package implements the approaches of Wichert et al. (2004),
Ahdesmaki et al. (2005) and Ahdesmaki et al. (2007) for detecting
periodically expressed genes from gene expression time series data.

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
%doc %{rlibdir}/GeneCycle/html
%doc %{rlibdir}/GeneCycle/DESCRIPTION
%doc %{rlibdir}/GeneCycle/doc
%{rlibdir}/GeneCycle/R
%{rlibdir}/GeneCycle/LICENSE
%{rlibdir}/GeneCycle/INDEX
%{rlibdir}/GeneCycle/Meta
%{rlibdir}/GeneCycle/help
%{rlibdir}/GeneCycle/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora