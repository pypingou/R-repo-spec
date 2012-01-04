%global packname  gaia
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          GAIA: An R package for genomic analysis of significant chromosomal aberrations.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-qvalue 

BuildRequires:    R-devel tex(latex) R-qvalue 

%description
This package allows to assess the statistical significance of chromosomal

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
%doc %{rlibdir}/gaia/html
%doc %{rlibdir}/gaia/doc
%doc %{rlibdir}/gaia/DESCRIPTION
%{rlibdir}/gaia/help
%{rlibdir}/gaia/INDEX
%{rlibdir}/gaia/Meta
RPM build errors:
%{rlibdir}/gaia/data
%{rlibdir}/gaia/R
%{rlibdir}/gaia/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora