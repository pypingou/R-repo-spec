%global packname  XhybCasneuf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          EBI/PSB cross-hybridisation study package

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-ath1121501cdf R-tinesath1cdf R-RColorBrewer R-methods R-grid 


BuildRequires:    R-devel tex(latex) R-affy R-ath1121501cdf R-tinesath1cdf R-RColorBrewer R-methods R-grid



%description
Cross-hybridisation study on the ATH1 Affymetrix GeneChip

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
%changelog
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora